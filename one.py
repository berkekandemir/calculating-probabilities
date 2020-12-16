# -*- coding: utf-8 -*-
"""
Created on Mon Apr 6 13:11:43 2020

@author: Berke Can Kandemir
"""
import matplotlib.pyplot as plotter # I used it to plot the graph
import numpy # I used that to create a range with floating numbers

p = []
q = []
variance = []

for i in numpy.arange(0,1.001,0.001): # In Bernoulli distribution,
    p.append(i) # total probability is 1. So, according to that knowledge,
    q.append(1 - i) # I created this equation. P can be anything between 0 and 1
                # and q will be 1 - p. I used 0.001 as the interval to have a preciser graph.

for i in range(len(p)):
    variance.append(p[i]*q[i]) # In Bernoulli distribution, var[x] is p*q.
    
plotter.plot(p,variance) # Then I draw the graph here with the data,
plotter.xlabel("p") # with x-axis and
plotter.ylabel("Variance") # y-axis labels.
plotter.show()
    
