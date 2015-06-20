from drawBot import *

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