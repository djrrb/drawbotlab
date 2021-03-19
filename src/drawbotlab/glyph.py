from fontTools.pens.basePen import BasePen
from robofab.objects.objectsRF import RFont, RGlyph
from drawBot import *

class DrawBotPen(BasePen):
    """
    A pen that draws a glyph into a drawbot.
    I don't think this can deal with components or anything so be careful.
    """
    def _moveTo(self, coordinate):
        moveTo(coordinate)
    def _lineTo(self, coordinate):
        lineTo(coordinate)
    def _curveToOne(self, coordinate1, coordinate2, coordinate3):
        curveTo(coordinate1, coordinate2, coordinate3)
    def closePath(self):
        closePath()


def drawGlyph(glyph):
    """
    Mimics the in-RoboFont drawbot, but using DrawBotPen.
    """
    newPath()
    pen = DrawBotPen(glyph.getParent())
    glyph.draw(pen)
    drawPath()
    
def _getKernGroups(groups):
    leftKernGroups = {}
    rightKernGroups = {}
    leftKernNames = ['@public.kern1', '@MMK_L_']
    rightKernNames = ['@public.kern2', '@MMK_R_']
    for groupName, groupGlyphs in groups.items():
        for name in leftKernNames:
            if name in groupName:
                leftKernGroups[groupName] = groupGlyphs
        for name in rightKernNames:
            if name in groupName:
                rightKernGroups[groupName] = groupGlyphs
    return leftKernGroups, rightKernGroups
        
def _getGlyphNamesFromTextString(textString, f, showMissing='.notdef'):
    gnames = []
    m = f.getCharacterMapping()
    for char in textString:
        gname = m.get(ord(char))
        if gname:
            gnames.append(gname[0])
        elif showMissing:
            if f.has_key(showMissing):
                gnames.append(showMissing)
    return gnames

def ufoText(textString, pos, font, fontSize, showMissing='.notdef', kerning=True, draw=True):
    """
    A function that uses drawGlyph() to draw a string from a robofab object.
    
    It acts like DrawBot's text() function, but you pass the font and fontSize directly.
    
    It does not handle any advanced text layout or features. For that you
    should generate a font and use compositor.
    
    ufoText(u'Your text here.', (0, 0), font=f, fontSize=50, kerning=False)
    """
    # get glyph names
    gnames = _getGlyphNamesFromTextString(textString, font, showMissing)
    # before we begin, get kerning
    # there is probably a better way to do this
    # but for now we will explode kerning once so we don't ahve to 
    if kerning:
        explodedKerning = font.kerning.copy()
        explodedKerning.explodeClasses(*_getKernGroups(font.groups))
    save()
    # move to the position
    if draw: translate(*pos)
    save()
    # drawGlyph draws at 1 pt = 1 font unit. 
    scaleFactor = fontSize / font.info.unitsPerEm
    if draw: scale(scaleFactor)
    
    totalWidth = 0
    
    # loop through glyphs and draw them
    previousGname = None
    for gname in gnames:
        if kerning:
            kern = explodedKerning.get((previousGname, gname)) or 0
            translate(kern, 0)
            totalWidth += kern
            
        if draw: drawGlyph(font[gname])
        if draw: translate(font[gname].width, 0)
        totalWidth += font[gname].width
        previousGname = gname
    restore()
    restore()
    return totalWidth, fontSize

def ufoTextSize(textString, font, fontSize, kerning=True):
    """
    Just like textSize, but using a UFO.
    
    This is pretty dang inefficient, but such is life!
    """
    return ufoText(textString, font, fontSize, draw=False)
    
    
### BY JUST ####

import AppKit

_methodMap = {
    AppKit.NSMoveToBezierPathElement: "moveTo",
    AppKit.NSLineToBezierPathElement: "lineTo",
    AppKit.NSCurveToBezierPathElement: "curveTo",
    AppKit.NSClosePathBezierPathElement: "closePath",
}

def drawPathToPen(path, pen):
    didClosePath = True
    for i in range(path._path.elementCount()):
        instr, pts = path._path.elementAtIndex_associatedPoints_(i)
        methodName = _methodMap[instr]
        if methodName == "moveTo":
            if not didClosePath:
                # Previous contour was open, we should call pen.endPath()
                pen.endPath()
            didClosePath = False
        elif methodName == "closePath":
            didClosePath = True
        getattr(pen, methodName)(*pts)
    if not didClosePath:
        # The final subpath is open, we must still call endPath()
        pen.endPath()
