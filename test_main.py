import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_dice(self) : 
        a, b, mean=1., 6, 0
        for i in range(100) : 
           var = dice_roll()
           self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your dice_roll function has returned a number that is not an integer" )
           self.assertTrue( var>=a and var<=b, Your dice_roll function has returned a number that falls outside the desired range of values" )
           mean = mean + var
        mean = mean / 100
        var = 1/12*( (b-a+1)*(b-a+1) - 1 )
        bar = np.sqrt(var/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - 0.5*(b+a) )<bar, "your dice_roll function does not appear to be sampling from the correct distribution" )
        
   def test_histo(self) :
       mean_histo = 6*[0]
       for i in range(20) :
           this_histo = histo_estimate(100)
           for j in range(6) : mean_histo[j] = mean_histo[j] + this_histo[j]
  
       for j in range(6) : mean_histo[j] = mean_histo[j] / 20

       for i in range(6) :
           bar = np.sqrt( (1/6)*(1-(1/6))/20 )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean_histo[i] - (1/6) )<bar, "your histogram function does not appear to be sampling from the correct distribution" )
