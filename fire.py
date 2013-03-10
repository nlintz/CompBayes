import sys
sys.path.append("thinkbayes_modules")
import thinkbayes
import numpy
import math
import myplot
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
	findLikelihood(10, 100, 100)

	# hypos = xrange(0, 1001)
	# fire = Fire_distanceError(hypos)

	# fire.Update((100, 10))
	# fire.Update((105, 10.1))
	# fire.Update((101, 10))
	# fire.Update((102, 10.2))

	# myplot.Pmf(fire)
	# myplot.Show(xlabel='Fire Size', ylabel='Probability')



if __name__ == "__main__":
    main()
