from fontTools.pens.basePen import BasePen

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

def roundedRect(x, y, w, h, r=None, curvature=.552):
    """
    Draw a rounded rectangle.
    Acts like drawbot rect() but takes optional 
    radius and curvature arguments.
    
    r is measured in units. 
    Curvature is a value between 0 and 1.
    """
    # if no radius is defined, set it to 1/8 the shorter side
    if r == None:
        r = min(w, h) / 8
    # determine the bezier length
    bl = curvature * r
    # draw the path
    p = BezierPath()
    p.moveTo((x, y+r))
    p.lineTo((x, y+h-r))
    p.curveTo((x, y+h-r+bl), (x+r-bl, y+h), (x+r, y+h))
    p.lineTo((x+w-r, y+h))
    p.curveTo((x+w-r+bl, y+h), (x+w, y+h-r+bl), (x+w, y+h-r))
    p.lineTo((x+w, y+r))
    p.curveTo((x+w, y+r-bl), (x+w-r+bl, y), (x+w-r, y))
    p.lineTo((x+r, y))
    p.curveTo((x+r-bl, y), (x, y+r-bl), (x, y+r))
    p.closePath()
    drawPath(p)