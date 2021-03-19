from math import sin, cos, tan, pi
from math import lerp, norm, remap

class BaseCycle:
    """Define a numeric cycle. Putting this in an object means we don’t have to calculate these values for each frame. Just remember to bump() it!"""
    def __init__(self, length, minimum=0, maximum=0):
        self.length = length
        self.counter = 0
        self.minimum = minimum
        self.maximum = maximum
        
    def bump(self):
        self.counter += 1
        
class SinCycle(BaseCycle):
    def get(self):
        progress = sin(2 * pi * (self.counter)/self.length)
        return remap(progress, -1, 1, self.minimum, self.maximum)
        
class CosCycle(BaseCycle):
    def get(self):
        progress = cos(2 * pi * (self.counter)/self.length)
        return remap(progress, -1, 1, self.minimum, self.maximum)
        
class TanCycle(BaseCycle):
    def get(self):
        progress = tan(2 * pi * (self.counter)/self.length)
        return remap(progress, -1, 1, self.minimum, self.maximum)
        