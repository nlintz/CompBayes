import sys
sys.path.append("thinkbayes_modules")
import myplot
import thinkbayes

# def trianglePrior(mean):
# 	upperBound = mean*2
# 	lowerBound = 0
# 	suite = thinkbayes.Suite(xrange(lowerBound, upperBound+1))
# 	for x in range(lowerBound, mean+1):
# 		suite.Set(x, x)
# 	for x in range(mean+1, upperBound+1):
# 		suite.Set(x, upperBound-x) 
# 	suite.Normalize()
# 	return suite
def trianglePrior(mean, sigma):
	upperBound = int(mean*(1+sigma))
	lowerBound = int(mean*(1-sigma))
	mean = int(mean)
	suite = thinkbayes.Suite(xrange(lowerBound, upperBound+1))

	for x in range(lowerBound, mean+1):
		suite.Set(x, x-lowerBound)
	for x in range(mean+1, upperBound+1):
		suite.Set(x, upperBound-x) 
	suite.Normalize()
	return suite


def main():
	tp = trianglePrior(12, (1.0/3))
	myplot.Pmf(tp)
	myplot.Show()

if __name__ == "__main__":
	main()