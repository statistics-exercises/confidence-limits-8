try:
    from AutoFeedback.plotchecks import check_plot
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.plotchecks import check_plot

from AutoFeedback.plotclass import line
from AutoFeedback.funcchecks import check_func
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class errclass : 
   def get_lower(i) : 
       from scipy.stats import norm
       return ( lower[i] / norm.ppf(0.05) )**2

   def get_upper(i) :
       from scipy.stats import norm
       return ( upper[i] / norm.ppf(0.95) )**2

class UnitTests(unittest.TestCase) :
    def test_dice(self) : 
        inputs, variables = [], []
        for i in range(10) :
            inputs.append(())
            myvar = randomvar( 3.5, variance=35/12, vmin=1, vmax=6, isinteger=True )
            variables.append( myvar ) 
        assert( check_func("dice_roll",inputs, variables ) ) 

    def test_histo(self) :
        inputs, variables = [], []
        for i in range(1,5) : 
            inputs.append((i*100,))
            myvar = randomvar( 1/6, variance=(1/6)*(5/6)/(i*100), vmin=0, vmax=1, isinteger=False )
            variables.append( myvar )
        assert( check_func("histo_estimate", inputs, variables, calls=["dice_roll"] ) )      

    def test_lower(self) :
        inputs, variables = [], []
        for i in range(6) :
            inputs.append((i,))
            myvar = randomvar( 1/6, dist="chi2", variance=(1/6)*(5/6)/nsamples, isinteger=False)
            variables.append( myvar )
        assert( check_func("get_lower", inputs, variables, modname=errclass ) ) 

    def test_upper(self) :
        inputs, variables = [], [] 
        for i in range(6) :
            inputs.append((i,))
            myvar = randomvar( 1/6, dist="chi2", variance=(1/6)*(5/6)/nsamples, isinteger=False)
            variables.append( myvar )
        assert( check_func("get_upper", inputs, variables, modname=errclass ) )  

    def test_plot(self) :
        x = np.linspace(1,6,6)
        var = randomvar( 1/6, variance=(1/6)*(5/6)/(nresamples*nsamples), vmin=0, vmax=1, isinteger=False )
        line1=line( x, var )
        axislabels=["Outcome", "Fraction of occurances"] 
        assert(check_plot([line1],exppatch=line1,explabels=axislabels,explegend=False,output=True))
