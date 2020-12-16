#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:59:08 2020

@author: berke
"""

import numpy as np
from matplotlib import pyplot as plt

p200 = []
n200 = []

p800 = []
n800 = []

p3200 = []
n3200 = []

n = 40
p = 0.3
q = 1 - p
# generates a list with random variables
# according to binomial distribution rules
def binomial(N):   
    Y = []
    for j in range(N):
        X = []
        for i in range(n):
            u = np.random.rand()
            x = u<p
            X.append(x)
        y = sum(X)
        Y.append(y)
    return Y

def calculator(N):
    for i in range(1000):  
        result = binomial(N)
        x_hat  = n * p # mean
        sub = 0 # sub total for summation eq.
        for i in range(N): # calculates summation eq. in p_hat eq.
            xi = result[i]
            sub += (xi - x_hat) ** 2 
        estimated_p = 1 - ((1 / (N * x_hat)) * sub) # p_hat eq.
        estimated_n = x_hat / estimated_p # n_hat eq.
        
        if N == 200:
            p200.append(estimated_p)
            n200.append(estimated_n)
        elif N == 800:
            p800.append(estimated_p)
            n800.append(estimated_n)
        elif N == 3200:
            p3200.append(estimated_p)
            n3200.append(estimated_n)
    
    if N == 200:
        mean_p200 = np.mean(p200)
        mean_n200 = np.mean(n200)
        
        stdev_p200 = np.std(p200)
        stdev_n200 = np.std(n200)
        
        mean_p = mean_p200
        mean_n = mean_n200
        std_p = stdev_p200
        std_n = stdev_n200
        
    elif N == 800:
        mean_p800 = np.mean(p800)
        stdev_p800 = np.std(p800)
        
        mean_n800 = np.mean(n800)
        stdev_n800 = np.std(n800)
        
        mean_p = mean_p800
        mean_n = mean_n800
        std_p = stdev_p800
        std_n = stdev_n800
        
    elif N == 3200:
        mean_p3200 = np.mean(p3200)
        mean_n3200 = np.mean(n3200)
        
        stdev_p3200 = np.std(p3200)
        stdev_n3200 = np.std(n3200)
        
        mean_p = mean_p3200
        mean_n = mean_n3200
        std_p = stdev_p3200
        std_n = stdev_n3200
    
    print("Mean for estimated p for sample size of", N, "is", mean_p)
    print("Standard deviation for estimated p for sample size of", N, "is", std_p, "\n")
        
    print("Mean for estimated n for sample size of", N, "is", mean_n)
    print("Standard deviation for estimated n for sample size of", N, "is", std_n, "\n")

def main():
    calculator(200)
    calculator(800)
    calculator(3200)
    
    plt.title('Histogram for estimated p')
    plt.hist(p200, 100, alpha = 0.5, density = True)
    plt.hist(p800, 100, alpha = 0.5, density = True)
    plt.hist(p3200, 100, alpha = 0.5, density = True)
    plt.legend(["200", "800", "3200"], loc ="upper right")
    plt.show()
    
    plt.title('Histogram for estimated n')
    plt.hist(n200, 100, alpha = 0.5, density = True)
    plt.hist(n800, 100, alpha = 0.5, density = True)
    plt.hist(n3200, 100, alpha = 0.5, density = True)
    plt.legend(["200", "800", "3200"], loc ="upper right")
    plt.show()

main()