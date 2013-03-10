import math
def heatflux(Q, r, theta=0, X=.3):
	"""
	@param Q: hypothetical firesize
	@type Q: integer
	@param r: distance from fire (m)
	@type r: integer
	@param theta: angle of the sensor
	@type theta: integer
	@param X: radiative heat fraction
	@type X: integer
	"""

	flux = (math.cos(theta)*X*Q)/(4*math.pi*r**2)
	return flux