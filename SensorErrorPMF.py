import sys
sys.path.append("thinkbayes_modules")
import myplot
import thinkbayes
from heatflux import *

def SensorPMF(sigma):
	errorPMF = thinkbayes.MakeGaussianPmf(0, sigma, 2, n=201)
	return errorPMF

def main():
	ePMF = SensorPMF(.1)
	myplot.Pmf(ePMF)
	myplot.Show()

if __name__ == "__main__":
	main()