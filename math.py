# MATH HELPERS

def lerp(start, stop, amt):
	"""
	Get Interpolated value.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate.
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value
