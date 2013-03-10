import sys
sys.path.append("thinkbayes_modules")
import fire
import thinkbayes
import myplot
import math
import matplotlib.pyplot as pyplot
import numpy as np


def findLikelihood(q, r, hypo):
	Q = hypo
	distancePmf = thinkbayes.MakeGaussianPmf(r, 10, 2) #gaussian distribution of error
	qstarPmf = thinkbayes.Pmf()

	for  dist, p in distancePmf.Items():
		q = heatflux(Q, dist)
		qstarPmf.Set(q, p)

	myplot.Pmf(qstarPmf)
	# myplot.Pmf(distancePmf)
	myplot.Show()

	return hypo


def main():
	findLikelihood(10, 100, 100)
	# hypos = xrange(0, 1001)
	# fire = Fire_distanceError(hypos)

	# fire.Update((150, 1))
	# fire.Update((150, 1))
	# fire.Update((150, 1))
	# fire.Update((150, 1))

	# myplot.Pmf(fire)
	# myplot.Show(xlabel='Fire Size', ylabel='Probability')


class Fire_distanceError(thinkbayes.Suite):
	"""
	The fire class we use
	to generate a pmf of 
	our distance measurement accuracy
	"""
	def Likelihood(self, hypo, data):
		"""
		@param hypo: the range of hypothesis
		used to generate a prior
		@type hypo: xrange
		@param data: the values for
		heatflux and distance from the fire (q, r)
		@type data: tuple
		"""
		q = data[0]
		r = data[1]

		
		like = findLikelihood(q, r, hypo)
		return like


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


if __name__ == "__main__":
    main()
    