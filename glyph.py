from fontTools.pens.basePen import BasePen
from robofab.objects.objectsRF import RFont, RGlyph
from drawBot import *

class DrawBotPen(BasePen):
    """
    A pen that draws a glyph into a drawbot.
    I don't think this can deal with components or anything so be careful.
    """
    def _moveTo(self, (x, y)):
        moveTo((x, y))
    def _lineTo(self, (x, y)):
        lineTo((x, y))
    def _curveToOne(self, (x1, y1), (x2, y2), (x3, y3)):
        curveTo((x1, y1), (x2, y2), (x3, y3))
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