import sys
sys.path.append("thinkbayes_modules")
import fire
import thinkbayes
import myplot
import math
import matplotlib.pyplot as pyplot
import numpy as np


def findLikelihood(q, r, hypo):
	distancePmf = thinkbayes.MakeGaussianPmf(r, 20, 3) #gaussian distribution of error
	distanceDict = distancePmf.GetDict() #dictionary of this pmf, easier to use
	q_starDict = {} #dictionary representing the qstar pmf
	distances = sorted(distanceDict.keys()) #array of distances
	P = [distanceDict[i] for i in distances] #'sorted' probabilities

	q_starDist = sorted([heatflux(hypo, i) for i in distances]) #values for the qstar distribution
	q_starPmf = pyplot.plot(q_starDist, P) #pmf is a matplotlib plot object

	q_starValues = q_starPmf[0].get_xdata()
	likelihoodValues = q_starPmf[0].get_ydata()
	qData = np.where(q_starValues==q_starValues[q])
	return likelihoodValues[qData][0]


def main():
	hypos = xrange(0, 1001)
	fire = Fire_distanceError(hypos)

	fire.Update((100, 10))
	fire.Update((105, 10.1))
	fire.Update((101, 10))
	fire.Update((102, 10.2))

	myplot.Pmf(fire)
	myplot.Show(xlabel='Fire Size', ylabel='Probability')


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
    