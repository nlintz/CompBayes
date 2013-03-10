import sys
sys.path.append("thinkbayes_modules")
import thinkbayes
import numpy
import scipy.stats
import myplot
import pylab
import matplotlib.pyplot as pyplot
import numpy as np
from heatflux import *
from Fire_SensorError import *
from Fire_DistanceError import *

'''
This class will account for fire size given an uncertain
measurement distance
'''
def main():
	hypos = xrange(100, 1001)
	fire_DistanceError = Fire_DistanceError(hypos)

	fire_DistanceError.Update((.19, 10))
	fire_DistanceError.Update((.192, 10))
	fire_DistanceError.Update((.192, 10))
	fire_DistanceError.Update((.20, 10))

	fire_SensorError = Fire_SensorError(hypos)

	fire_SensorError.Update((.19, 10))
	fire_SensorError.Update((.192, 10))
	fire_SensorError.Update((.192, 10))
	fire_SensorError.Update((.20, 10))

	randomSamples = []
	for i in range(500):
		randomSamples.append(fire_DistanceError.Random())
		randomSamples.append(fire_SensorError.Random())
		
	randomSamples.append(.1) #this is super weird

	kde = scipy.stats.gaussian_kde(randomSamples)
	evalkde = kde.evaluate(hypos)
	print randomSamples
	print evalkde

	# myplot.Pmf(fire_SensorError)
	# myplot.Pmf(fire_DistanceError)
	pylab.plot(hypos, evalkde)
	# myplot.Show()
	pylab.show()


	# myplot.Pmf(fire_SensorError)
	# myplot.Show(xlabel='Fire Size', ylabel='Probability')



if __name__ == "__main__":
    main()
