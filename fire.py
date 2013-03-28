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
from SensorErrorPMF import *

'''
This class will account for fire size given an uncertain
measurement distance
'''
def main():
	hypos = xrange(100, 1001)
	fire_DistanceError = Fire_DistanceError(hypos)

	# fire_DistanceError.Update((.19, 10))
	# fire_DistanceError.Update((.192, 10))
	# fire_DistanceError.Update((.192, 10))
	# fire_DistanceError.Update((.20, 10))

	# fire_SensorError = SensorPMF(1)
	
	# randomSamples = []
	# for i in range(1000):
	# 	randomSamples.append(fire_DistanceError.Random()+fire_SensorError.Random())
		
	# kde = scipy.stats.gaussian_kde(randomSamples)
	# evalkde = kde.evaluate(hypos)

	# myplot.Pmf(fire_SensorError)
	myplot.Pmf(fire_DistanceError)
	# myplot.Pmf(fire_SensorError)
	myplot.Show(xlabel='Fire Size (kilowatts)', ylabel='Probability')

	# myplot.Show()
	# pylab.xlabel('Fire Size (kilowatts)')
	# pylab.ylabel('Probability')
	# pylab.plot(hypos, evalkde)
	# pylab.show()





if __name__ == "__main__":
    main()
