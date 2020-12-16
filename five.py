#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:11:52 2020

@author: berke
"""

import numpy as np
#import math
from matplotlib import pyplot as plt
import statistics
#from scipy.stats import norm
import random

numSamples = 100000
numBins = 100

#def normalDist(x, stdev, mean):
#    return math.exp((-(x - mean) ** 2) / (2 * (stdev ** 2))) / (stdev * math.sqrt(math.pi))

def first(value):
    domain = np.linspace(-1, 3, 1000)
    sums = []
    U = []
    stdev = 0
    mean = 0
#    normal_dist = []
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = np.random.uniform(0, 1)
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
 #   for i in sums:    
 #       normal_dist.append(normalDist(i, stdev, mean))
    
    print("Experiment 1:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
        
    #plt.figure()
    plt.title('Histograms for generated random variables')
    plt.hist(U, numBins, density = True)
    plt.show()
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    #plt.plot(domain, norm.pdf(domain, mean, stdev))
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    #plt.plot(bins, normalDist(bins, stdev, mean))
    plt.show()
    
def second(value):
    domain = np.linspace(0.5, 9.5, 1000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = np.random.uniform(0, 1)
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 2:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
def third(value):
    domain = np.linspace(14.8, 35.2, 1000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = np.random.uniform(0, 1)
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 3:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
first(2)
#second(10)
#third(50)

def fourth(value):
    domain = np.linspace(35, 49, 1000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            if total < 40:
                temp = np.random.uniform(0.5, 1.5)
            else:
                temp = np.random.uniform(-0.5, 0.5)
            U.append(temp)
            total += temp
        sums.append(total)
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 4:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histograms for generated random variables')
    plt.hist(U, numBins, density = True)
    plt.show()
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
#fourth(100)

def semicircle_distribution(domain):
    choice = random.choice(domain)
    return np.sqrt(1 - ((choice - 2) ** 2))

def fifth(value):
    domain = np.linspace(0.5, 7.5, 1000)
    domain2 = np.linspace(1, 3, 20000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = semicircle_distribution(domain2)
            #temp = semicircle(np.random.uniform(1, 3))
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 5:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histograms for generated random variables')
    plt.hist(U, numBins, density = True)
    plt.show()
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
def sixth(value):
    domain = np.linspace(12, 28, 1000)
    domain2 = np.linspace(1, 3, 20000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = semicircle_distribution(domain2)
            #temp = semicircle(np.random.uniform(0, 1))
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 6:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
def seventh(value):
    domain = np.linspace(80, 120, 1000)
    domain2 = np.linspace(1, 3, 20000)
    sums = []
    U = []
    stdev = 0
    mean = 0
    for i in range(numSamples):
        total = 0
        for j in range(value):
            temp = semicircle_distribution(domain2)
            #temp = semicircle(np.random.uniform(0, 1))
            U.append(temp)
            total += temp
        sums.append(total)
    
    stdev = statistics.stdev(sums)
    mean = statistics.mean(sums)
    
    print("Experiment 7:")
    print("Sample mean is", mean)
    print("Sample standard deviation is", stdev)
    
    #plt.figure()
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sums, numBins, density = True)
    plt.plot(domain, ((1/(stdev * np.sqrt(2 * np.pi))) * np.exp((- (domain - mean)**2) / (2 * stdev**2))))
    plt.show()
    
#fifth(2)
#sixth(10)
#seventh(50)