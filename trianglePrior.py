import sys
sys.path.append("thinkbayes_modules")
import myplot
import thinkbayes

def trianglePrior():
	hypos = xrange(0, 101)
	suite = thinkbayes.Suite(hypos)
	for x in range(0, 51):
	   	suite.Set(x, x)
	for x in range(51, 101):
	   	suite.Set(x, 100-x) 
	suite.Normalize()

	return suite