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

	fire_DistanceError.Update((.19, 10))
	fire_DistanceError.Update((.192, 10))
	fire_DistanceError.Update((.192, 10))
	fire_DistanceError.Update((.20, 10))

	myplot.Pmf(fire_DistanceError)
	myplot.Show(xlabel='Fire Size (kilowatts)', ylabel='Probability')





if __name__ == "__main__":
    main()
