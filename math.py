# MATH HELPERS

def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate.
	Get Interpolated value, between zero and one.
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value
