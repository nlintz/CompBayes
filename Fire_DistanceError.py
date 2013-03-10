import sys
sys.path.append("thinkbayes_modules")

import myplot
import thinkbayes
from trianglePrior import *
from heatflux import *

class Fire_DistanceError(thinkbayes.Suite):
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
	distancePmf = trianglePrior(r, (1.0/3)) #gaussian distribution of error

	qstarPmf = thinkbayes.Pmf()

	for  dist, p in distancePmf.Items():
		qstar = heatflux(Q, dist)
		qstarPmf.Set(qstar, p)

	qstars = sorted(qstarPmf.GetDict().keys())
	qNearest = nearestNeighbor(qstars, q)
	qstar = qstars[qNearest]

	# if qstar > q:
	# 	right = qstarPmf.Prob(qstar)
	# 	left = qstarPmf.Prob(qstars[qNearest-1])
	# 	like = (right+left)/2
	
	# else:
	# 	left = qstarPmf.Prob(qstar)
	# 	right = qstarPmf.Prob(qstars[qNearest+1])
	# 	like = (right+left)/2
	like = qstarPmf.Prob(qstar)
	return like

def nearestNeighbor(lst, val):
	indices = range(len(lst))
	return min(indices, key=lambda x: abs(lst[x]-val))

def main():
	findLikelihood(.4, 8, 1000)

if __name__ == "__main__":
	main()



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
