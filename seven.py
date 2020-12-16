#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:29:10 2020

@author: berke
"""

import random
import numpy as np
from matplotlib import pyplot as plt

crew = []
first = []
second = []
third = []

file = open("titanic_data.txt", "r")
for x in file:
    elements = x.split("	")
    if elements[0] == "0":
        crew.append(int(elements[1]))
    elif elements[0] == "1":
        first.append(int(elements[1]))
    elif elements[0] == "2":
        second.append(int(elements[1]))
    elif elements[0] == "3":
        third.append(int(elements[1]))
file.close()

mean_all = (sum(crew) + sum(first) + sum(second) + sum(third)) / (len(crew) + len(first) + len(second) + len(third))
mean_crew = sum(crew) / len(crew)
mean_first = sum(first) / len(first)
mean_second = sum(second) / len(second)
mean_third = sum(third) / len(third)
mean_rest_of_first = (sum(crew) + sum(second) + sum(third)) / (len(crew) + len(second) + len(third))

print("\nThe averages for the whole data, crew data, first class, second class and third class data are %.2f, %.2f, %.2f, %.2f and %.2f, respectively." %(mean_all, mean_crew, mean_first, mean_second, mean_third))

# for question 1

differences_pdf = []
for i in range(10000):
    mergedList = crew + third
    random.shuffle(mergedList)
    new_crew = []
    index = 0
    for j in range(len(crew)):
        new_crew.append(mergedList[index])
        del mergedList[index]
    new_third = mergedList
    mean_new_crew = np.mean(new_crew)
    mean_new_third = np.mean(new_third)
    differences_pdf.append(mean_new_crew - mean_new_third)

count, bins, ignored = plt.hist(differences_pdf, 100, density = False)
plt.show()

cdf = np.cumsum(count) / sum(count)
bins = np.delete(bins, 100)
plt.plot(bins, cdf)

x = mean_crew - mean_third
for i in range(len(bins)):
    if bins[i] >= x:
        index = i
        break

plt.plot([x, x], [0, cdf[index]])
plt.show()
# cdf[index] might not be the same for every run. It changes because we use bins = 100.
# For more accurte result, we should use greater bins value but the graph looks ugly then.
print("\nThe p-value for %.2f difference and less between means for crew and 3rd class is %.2f." %(x, cdf[index]))

# for question 2

differences_pdf = []
for i in range(10000):
    mergedList = first + crew + second + third
    random.shuffle(mergedList)
    new_first = []
    index = 0
    for j in range(len(first)):
        new_first.append(mergedList[index])
        del mergedList[index]
    rest = mergedList
    mean_new_first = np.mean(new_first)
    mean_new_rest_of_first = np.mean(rest)
    differences_pdf.append(mean_new_first - mean_new_rest_of_first)

count, bins, ignored = plt.hist(differences_pdf, 100, density = False)
plt.show()

cdf = np.cumsum(count) / sum(count)
bins = np.delete(bins, 100)
plt.plot(bins, cdf)

x = mean_first - mean_rest_of_first
for i in range(len(bins)):
    if bins[i] >= x:
        index = i
        break

plt.plot([x, x], [0, cdf[index]])
plt.show()

print("\nThe p-value for %.2f difference and more in means for 1st class and the rest is %.2f." %(x, cdf[index]))






    