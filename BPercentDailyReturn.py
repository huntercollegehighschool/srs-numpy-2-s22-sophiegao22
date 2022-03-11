""" 
Percent Daily Return Exercise

In this exercise, you are given the stock values for several consecutive days for acme corporation. Your job is to calculate the "percent daily return" for each day. The percent daily return is the percentage that the stock changes each compared to the day before.

Note: the percent daily return = 100 * (current day - previous day)/previous day

Below you are given the stock prices (there are only 4 days in this example). First convert to a numpy array. Then use slicing and numeric operations to calculate the percent daily return (no for loops!).
"""
import numpy as np
acme = [10, 11.5, 11, 10, 12]
acmearray = np.array(acme)

acmearray[4] = acmearray[4]-acmearray[3]
acmearray[3] = acmearray[3]-acmearray[2]
acmearray[2] = acmearray[2]-acmearray[1]
acmearray[1] = acmearray[1]-acmearray[0]


print(acmearray)

acmearray4 = np.delete(acmearray, 0)

print(acmearray4)

multipliedacme = 100*acmearray4

print(multipliedacme)

newacmearray = np.array(acme)

print(newacmearray)

multipliedacme[0] = multipliedacme[0]/newacmearray[0]
multipliedacme[1] = multipliedacme[1]/newacmearray[1]
multipliedacme[2] = multipliedacme[2]/newacmearray[2]
multipliedacme[3] = multipliedacme[3]/newacmearray[3]

print(multipliedacme)