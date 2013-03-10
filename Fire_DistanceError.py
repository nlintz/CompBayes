import sys
sys.path.append("thinkbayes_modules")

import myplot
import thinkbayes
import 
from heatflux import *

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

# def findLikelihood(q, r, hypo):
# 	distancePmf = thinkbayes.MakeGaussianPmf(r, 20, 3) #gaussian distribution of error
# 	distanceDict = distancePmf.GetDict() #dictionary of this pmf, easier to use
# 	q_starDict = {} #dictionary representing the qstar pmf
# 	distances = sorted(distanceDict.keys()) #array of distances
# 	P = [distanceDict[i] for i in distances] #'sorted' probabilities

# 	q_starDist = sorted([heatflux(hypo, i) for i in distances]) #values for the qstar distribution
# 	q_starPmf = pyplot.plot(q_starDist, P) #pmf is a matplotlib plot object
# 	# pyplot.show()
# 	q_starValues = q_starPmf[0].get_xdata()
# 	likelihoodValues = q_starPmf[0].get_ydata()
# 	qData = np.where(q_starValues==q_starValues[q])
# 	return likelihoodValues[qData][0]
