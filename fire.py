import sys
sys.path.append("thinkbayes_modules")
import thinkbayes
import numpy
import math
import myplot

'''
This class will account for fire size given an uncertain
measurement distance
'''

class Fire(thinkbayes.Suite):
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

		q_star = fireSize(q, r) #Expected firesize
		lam = hypo-q_star

		like = thinkbayes.EvalGaussianPdf(0, 50, lam)
		return like



def fireSize(q, r, theta=0, X=.3):
	"""
	@param q: heat flux data from sensor (kW/m^2)
	@type q: integer
	@param r: distance from fire (m)
	@type r: integer
	@param theta: angle of the sensor
	@type theta: integer
	@param X: radiative heat fraction
	@type X: integer
	"""

	firesize = (q*4*math.pi*r**2)/(math.cos(theta)*X)
	return firesize


if __name__ == "__main__":
    hypos = xrange(100, 1001)
    fire = Fire(hypos)

    fire.Update((6.2, .6))
    fire.Update((6.3, .6))
    fire.Update((6.1, .6))
    fire.Update((6.0, .6))
    fire.Update((100, .6))

    myplot.Pmf(fire)
    myplot.Show(xlabel='Fire Size',
                ylabel='Probability')
