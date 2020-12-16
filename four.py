#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:29:52 2020

@author: berke can kandemir
"""

import random
from numpy import sqrt

# Simulates the game, rolls dices and according to the results, return true or false
def gameSimulator():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    firstDice = dice1 + dice2
    first = True
    while True:
        if first:
            if firstDice == 7 or firstDice == 11:
                return True
            elif firstDice == 2 or firstDice == 3 or firstDice == 12:
                return False
            else:
                first = False
        else:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice = dice1 + dice2
            if firstDice == dice:
                return True
            elif dice == 7:
                return False

# By the given rules, plays the game and return the gain of gambler A
def gambler_A(initial_money):
    balance = initial_money
    play = True
    bet = 1
    while play:
        if gameSimulator():
            balance += bet
            if balance >= (initial_money * 2):
                play = False
        else:
            balance -= bet
            bet *= 2
            if balance < bet or balance == 0:
                play = False
    result = balance - initial_money
    return result

# CDF of fx = u = Fx(x) = x^2 / r^2
# Inverse of cdf = x = sqrt(u * r^2)
# From the calculations, u should be 0 < u < 1

# Finds F^(-1)(x) for the given round number.
def Fx_inverse(r):
    u = random.random()
    return sqrt(u * (r**2))

# By the given rules for gambler B, plays the game and return the gain
def gambler_B(initial_money):
    balance = initial_money
    gain = 0
    play = True
    r = 1
    while play:
        bet = Fx_inverse(r)
        if gameSimulator():
            gain += bet
            balance += bet
            if gain >= 500:
                play = False
        else:
            gain -= bet
            balance -= bet
            if balance < bet or balance == 0:
                play = False
        r += 1
    result = balance - initial_money
    return result

# 100000 times plays the game and finds the winning count
# By the ratio, finds the probability of winning in the craps game            
sumList = []     
for i in range(100000):
    sumList.append(gameSimulator())
result = sum(sumList)
print("1. Probability of winning a round in craps:", result/100000)

# 100000 times plays as gambler A with $1000 and by the ratio, finds the expected gain            
expected_1 = 0
for i in range(100000):
    expected_1 += gambler_A(1000)
print("2. Expected gain of gambler A for $1.000: $" + str(expected_1/100000))


# 100000 times plays as gambler A with $1000000 and by the ratio, finds the expected gain  
expected_2 = 0
for i in range(100000):
    expected_2 += gambler_A(1000000)
print("3. Expected gain of gambler A for $1.000.000: $" + str(expected_2/100000))


# 100000 times plays as gambler B with $100 and by the ratio, finds the expected gain  
expected_3 = 0
for i in range(100000):
    expected_3 += gambler_B(100)
print("4. Expected gain of gambler B for $100: $" + str(expected_3/100000))


# 100000 times plays as gambler B with $10000 and by the ratio, finds the expected gain  
expected_4 = 0 
for i in range(100000):
    expected_4 += gambler_B(10000)
print("5. Expected gain of gambler B for $10.000: $" + str(expected_4/100000))    