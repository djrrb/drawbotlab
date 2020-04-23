from drawBot import *

def roundedRect(x, y, w, h, r=None, curvature=.6):
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
    
    
def fillRect(shape, cx, cy, cw, ch, shapeScale=1, cols=None, rows=None, gap=None, clip=False):

    save()
    if clip:
        clip = BezierPath()
        clip.rect(cx, cy, cw, ch)
        clipPath(clip)
    
    x1, y1, x2, y2 = shape.bounds()
    shapeWidth = (x2 - x1) * shapeScale
    shapeHeight = (y2 - y1) * shapeScale
    

    if gap is None and not cols and not rows:
        print ('Set columns and rows or an object gap.')
    elif gap is not None and not cols and not rows:
        cols = cw / (shapeWidth+gap)
        if cols != int(cols):
            cols += 1
        cols = int(cols)

        rows = ch / (shapeHeight+gap)
        if rows != int(rows):
            rows += 1
        rows = int(rows)
        print (cols, rows)

    elif gap:
        print ('Ignoring gap...')

    if gap:
        gapx = gap
        gapy = gap
    else:
        gapx = (cw-shapeWidth*(cols-1))/(cols-1)
        gapy = (ch-shapeHeight*(rows-1))/(rows-1)

    translate(-shapeWidth/2, -shapeHeight/2)

    translate(cx, cy)
    
    for r in range(rows):
        save()
        for c in range(cols):
            save()
            scale(shapeScale)
            drawPath(shape)
            restore()
            translate(shapeWidth+gapx, 0)
        restore()
        translate(0, shapeHeight+gapy)
    restore()
