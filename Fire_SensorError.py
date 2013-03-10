import sys
sys.path.append("thinkbayes_modules")
import myplot
import thinkbayes
from heatflux import *
class Fire_sensorError(thinkbayes.Suite):
	"""
	The fire class we use
	to generate a pmf of 
	our sensor's accuracy
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

		q_star = heatflux(hypo, r)
		error = q-q_star

		like = thinkbayes.EvalGaussianPdf(0, 50, error)
		return like