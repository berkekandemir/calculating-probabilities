#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:02:59 2020

@author: Berke Can Kandemir
"""

import numpy as np
from matplotlib import pyplot as plt
import operator as op
from functools import reduce

# def combination(n, r):
#    r = min(r, n-r)
#    numerator = reduce(op.mul, range(n, n-r, -1), 1)
#    denominator = reduce(op.mul, range(1, r+1), 1)
#    return numerator / denominator

# 1 - Binomial Sub-interval
# def BinomialEq(n,p,x):
#    binomial = combination(n,x)*(p**x)*((1-p)**(n-x))
#    return binomial

# p = 0.6
# Y = []
# X = []

# for j in range(1000):
#    X.append(j)
#    k = BinomialEq(1000, p, j)
#    Y.append(k)
    
# plt.title("Binomial Sub-intervalHistogram")
# plt.bar(X,Y)
# plt.show()


# 2.a - Geometric Bernoulli
p = np.random.rand()
count = 0
N = 20
fail = []
for j in range(500):
    X = []
    for k in range(N):
        u = np.random.rand()
        if u < p: 
            fail.append(count)
            count = 0
        count += 1

plt.figure()
plt.hist(fail, 100, density=True)
plt.title("Geometric Bernoulli Histogram")
plt.show()


# 2.b - Geometric Sub-interval

# def GeometricEq(p,x):
#    geometric = ((1-p)**(x-1))*p
#    return geometric

# p = 0.01
# Y = []
# X = []

# for j in range(1000):
#    X.append(j)
#    k = GeometricEq(p, j)
#    Y.append(k)
    
# plt.title("Geometric Sub-interval Histogram")
# plt.bar(X,Y)
# plt.show()


# 3 - The Monty Hall Problem

switch_win = 0
stick_win = 0
for i in range(10000):
    prize = int(np.random.rand() * 3) + 1
    picked = int(np.random.rand() * 3) + 1
    print("- Door number", picked, "selected.")
    opened = picked
    while picked == opened:
        opened = int(np.random.rand() * 3) + 1
        while prize == opened:
            opened = int(np.random.rand() * 3) + 1
    print("- Door number", opened, "opened.")
    print("- Do you want to switch or stick?")
    choice_maker = np.random.randint(2)
    if choice_maker == 0:
        choice = "switch"
        old_picked = picked
        while picked == old_picked:
            picked = int(np.random.rand() * 3) + 1
            while picked == opened:
                picked = int(np.random.rand() * 3) + 1
        print("- Door switched to" + str(picked) + ".")
    else:
        choice = "stick"
        print("- Door didn't switched.")
    if picked == prize:
        print("- You won the car!")
        if choice == "switch":
            switch_win += 1
        else:
            stick_win +=1
    else:
        print("- You missed the prize!")
        if choice == "switch":
            stick_win += 1
        else:
            switch_win += 1
    print("\n")

switch_win_rate = (switch_win / 10000) * 100
stick_win_rate = (stick_win / 10000) * 100

print("Winning rate of switching: %", (switch_win_rate))
print("Winning rate of sticking: %", (stick_win_rate))



















