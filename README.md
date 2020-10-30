# Histograms and Percentiles

Having demonstrated that we remember how to compute a histogram let's now write suitable code to generate the error bars on the estimates of the probability that we extract by resampling.

Although I have done a lot of the work for you here you still have to do a few things; namely:

1. You have to write a function called `dice_roll` that returns the (random) outcome of a roll of a fair six-sided dice.
2. You need to write a function called `histo_esimtate` that takes a parameter called `n`.   Within this function, you should compute a histogram by taking `n` samples using your `dice_roll` function.  The fraction of times you get each of the six possible outcomes on rolling the dice should be stored in the array called `histo`, which will be returned from your function. 

When you have written these functions and the code is run a graph showing the histogram with suitable error bars on each of the bars in this is produced.  Look at the code that I have written on the left and try to understand how it works.  We are only using ideas about percentiles that you have learned about in this course.  It is a little more complicated, however, as we have to use two dimensional NumPy arrays as we are estimating multiple random variables simultaneously.
