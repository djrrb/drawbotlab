from drawBot import *
"""
I find dealing with color tuples in drawbot to be cumbersome. 
Usually, I'd rather deal with colors as a single object, rather than
tuples or individual r/g/b/a elements that I have to pass individually
to the fill() or stroke() function.

fillColor() and fillStroke() will accept a unified tuple, RGBColor, 
or CMYKColor object. That means if you switch from RGB to CMYK,
I don't have to find every instance of fill() in my code.

"""

class RGBColor:
	"""
	A simple RGB color object.
	"""
	def __init__(self, r=0, g=0, b=0, a=1):
		self.r = r
		self.g = g
		self.b = b
		self.a = a
		self.colorMode = 'RGB'
	
	def asTuple(self):
		return (self.r, self.g, self.b, self.a)
	
	def setFill(self):
		fill(self.r, self.g, self.b, self.a)
	
	def setStroke(self):
		stroke(self.r, self.g, self.b, self.a)
		
class CMYKColor:
	"""
	A simple CMYK color object.
	"""
	def __init__(self, c=0, m=0, y=0, k=0, a=1):
		self.c = c
		self.m = m
		self.y = y
		self.k = k
		self.a = a
		self.colorMode = 'CMYK'
	
	def asTuple(self):
		return (self.c, self.m, self.y, self.k, self.a)
	
	def setFill(self):
		fill(self.c, self.m, self.y, self.k, self.a)
	
	def setStroke(self):
		cmykFill(self.c, self.m, self.y, self.k, self.a)
	

def fillColor(c, mode='RGB'):
    """
    a helper function that processes rgba or cymka tuples. 
    I use this because I hate having to switch back and forth between
    color spaces, and splitting up colors from tuples each time.
    """
    
    # if we are using a color object (defined above), use the object's fill method
    if hasattr(c, 'colorMode'):
    	c.setFill()
    
    # if we are passed an integer or float, set it as a simple RGB.
    elif isinstance(c, (int, float)):
    	fill(c, c, c)
    	
    # if we are dealing with a CMYKA tuple, set it
    elif len(c) == 5:
        cmykFill(c[0], c[1], c[2], c[3], c[4])
        
    # if we have a CMYK tuple and mode is set to CMYK
    elif len(c) and mode.upper() == 'CMYK':
    	cmykFill(c[0], c[1], c[2], c[3])
    	
    # otherwise we will assume that four-item tuples are RGBA
    elif len(c) == 4:
        fill(c[0], c[1], c[2], c[3])
        
    # last but not least, RGB!
    elif len(c) == 3:
        fill(c[0], c[1], c[2])
    
    
def strokeColor(c, mode='RGB'):
    """
    Just like fillColor, but for strokes!
    """
    
    # if we are using a color object (defined above), use the object's fill method
    if hasattr(c, 'colorMode'):
    	c.setStroke()
    
    # if we are passed an integer or float, set it as a simple RGB.
    elif isinstance(c, (int, float)):
    	stroke(c, c, c)
    	
    # if we are dealing with a CMYKA tuple, set it
    elif len(c) == 5:
        cmykStroke(c[0], c[1], c[2], c[3], c[4])
    
    # a four-element tuple can either be RGBA or CMYK.
    
    # if we have explicitly set the mode to CMYK, do that
    elif len(c) and mode.upper() == 'CMYK':
    	cmykStroke(c[0], c[1], c[2], c[3])
    	
    # otherwise we will assume that four-item tuples are RGBA
    elif len(c) == 4:
        stroke(c[0], c[1], c[2], c[3])
        
    # last but not least, RGB!
    elif len(c) == 3:
        stroke(c[0], c[1], c[2])