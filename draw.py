import drawBot 

def imageBox(im, box, fit="fill", clip=False, center=None, alpha=1):
    """
    Draw an image object in a given rectangle.
    """
    # if given a string, make an image object
    if isinstance(im, str):
        im = ImageObject(im)
    boxX, boxY, boxW, boxH = box
    # get the image dimensions
    imW, imH = im.size()
    imX, imY = boxX, boxY
    # if a center is not provided, use the center of the image
    if center is None:
        center = imW/2, imH/2
    # get the relative scale of image to box in both directions 
    fitScaleX = boxW/imW
    fitScaleY = boxH/imH
    # make the transformations
    with savedState():
        translate(boxX, boxY) 
        # if fit is "cover", make a clipping path
        if clip or (fit == "cover" and clip is None):
            b = BezierPath()
            b.rect(0, 0, boxW, boxH)
            clipPath(b)
        # use the center of the box as a starting point
        offsetX = boxW/2
        offsetY = boxH/2
        # the scale we will actually use
        scaleX = 1
        scaleY = 1
        # if fit is "cover", use the maximum fit
        if fit == 'cover':
            scaleX = scaleY = max(fitScaleX, fitScaleY)
        # if fit is "contain", use the minimum fit
        elif fit == "contain":
            scaleX = scaleY = min(fitScaleX, fitScaleY)
        elif fit == "scale-down":
            contain = min(fitScaleX, fitScaleY)
            scaleX = scaleY = min(contain, 1)
        # if fit is "none", do nothing 
        elif fit == "none":
            pass
        else:
            # by default, fit in both directions
            scaleX = fitScaleX
            scaleY = fitScaleY
        # move to the center
        translate(offsetX, offsetY)
        # scale depending on fit
        scale(scaleX, scaleY)
        # draw the image centered on the center point
        image(im, (-center[0], -center[1]), alpha=alpha)
    # draw the center point
    DEBUG = False
    if DEBUG:
        with savedState():
            fill(0, 1, 0)
            oval(boxX+offsetX-5, boxY+offsetY-5, 10, 10)

    

def pathBox(path, box, fit="fill", clip=False, center=None):
    """
    Draw a BezierPath in a given rectangle.
    """
    boxX, boxY, boxW, boxH = box
    # get the image dimensions
    xMin, yMin, xMax, yMax = path.bounds()
    imW = xMax - xMin
    imH = yMax - yMin
    imX, imY = xMin, yMin
    # if a center is not provided, use the center of the image
    if center is None:
        center = imW/2, imH/2
    # get the relative scale of image to box in both directions 
    fitScaleX = boxW/imW
    fitScaleY = boxH/imH
    # make the transormations
    with savedState(): 
        translate(boxX, boxY)
        # if fit is "cover", make a clipping path
        if clip:
            b = BezierPath()
            b.rect(0, 0, boxW, boxH)
            clipPath(b)
        # use the center of the box as a starting point
        offsetX = boxW/2
        offsetY = boxH/2
        # the scale we will actually use
        scaleX = 1
        scaleY = 1
        # if fit is "cover", use the maximum fit
        if fit == 'cover':
            scaleX = scaleY = max(fitScaleX, fitScaleY)
        # if fit is "contain", use the minimum fit
        elif fit == "contain":
            scaleX = scaleY = min(fitScaleX, fitScaleY)
        elif fit == "scale-down":
            contain = min(fitScaleX, fitScaleY)
            scaleX = scaleY = min(contain, 1)
        # if fit is "none", do nothing 
        elif fit == "none":
            pass
        else:
            # by default, fit in both directions
            scaleX = fitScaleX
            scaleY = fitScaleY
        # move to the center
        translate(offsetX, offsetY)
        # scale depending on fit
        scale(scaleX, scaleY)
        # draw the image centered on the center point
        translate(-imX-center[0], -imY-center[1])
        drawPath(path)
    DEBUG = False
    if DEBUG:
        with savedState():
            fill(0, 1, 0)
            oval(boxX+offsetX-5, boxY+offsetY-5, 10, 10)

if __name__ == "__main__":
    path = "image.png"
    for fit in ['fill', 'contain', 'scale-down', 'cover', 'none']:
        newPage(1000, 500)
        r = (200, 125, 200, 200)
        im = ImageObject(path)
        imageBox(im, r, fit=fit)
        with savedState():
            fill(None)
            stroke(1, 0, 0)
            strokeWidth(2)
            rect(*r)
        r = (600, 125, 200, 200)
        fs = FormattedString('a', fontSize=800, font='Condor Variable')
        b = BezierPath()
        b.text(fs)
        fill(0, 1, 0)
        pathBox(b, r, fit=fit)
        with savedState():
            fill(None)
            stroke(1, 0, 0)
            strokeWidth(2)
            rect(*r)
        fontSize(30)
        fill(0)
        text(fit, (width()/2, 380), align="center")
