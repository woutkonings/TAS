#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:07:02 2021

@author: woutkonings
"""

import pandas as pd
from random import choices
from numpy import mean
from statistics import stdev
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def bootstrap(series, sampleSize):
    """
    

    Parameters
    ----------
    series : Series / list / array
        Series or array that one bootstraps from
    sampleSize : TYPE
        sample size of the new bootstrap sample

    Returns
    -------
    newSeries : list
        bootstrap sample

    """
    
    newSeries = choices(series, k = sampleSize)    
    
    return newSeries


""" Question 1 """

#read data and do scatterplot
df1 = pd.read_csv("Q1.csv")
df1.plot('x', 'y', kind = 'scatter')

###Q1.1 
#The probability of this happening is (1/n)^10

###Q1.2

#get the x values
x1 = df1.loc[:,'x']
y1 = df1.loc[:,'y']


#bootstrap 5 samples
for i in range(5):
    bootstrapSample = bootstrap(x1, len(x1))
    print(bootstrapSample)


###Q1.3  TODO: answer theoretical question

pluginTheta = mean(x1) / mean(y1)

###Q1.4

#make list to store theta values in  and sample 200 values of theta
thetaList = []
for i in range(200):
    bootstrapX = bootstrap(x1, len(x1))
    bootstrapY = bootstrap(y1, len(y1))
    thetaList.append( mean(bootstrapX) / mean(bootstrapY))

#plot histogram
plt.figure()
sns.histplot(thetaList)
plt.savefig('Q1 theta histogram')
meanTheta = mean(thetaList)

#calculate bias and standard error
bias = mean(thetaList) - pluginTheta
se = stdev(thetaList)


###Q1.5
biasList = []
seList = []

for i in range(100):
    print(i)
    thetaList = []
    for j in range(200):
        bootstrapX = bootstrap(x1, len(x1))
        bootstrapY = bootstrap(y1, len(y1))
        thetaList.append( mean(bootstrapX) / mean(bootstrapY))
    
    #calculate bias and standard error and add to result list
    biasList.append(mean(thetaList) - pluginTheta)
    seList.append(stdev(thetaList))

#show bias histogram
plt.figure()
sns.histplot(biasList)
plt.savefig('Q1 bias histogram')
#show standard arror histogram
plt.figure()
sns.histplot(seList)
plt.savefig('Q1 standard errors histogram')


#The estimator looks like it is biased from the histogram.


###Q1.6
# I think because Y has two heavy outliers, the bootstrap has strong downward bias.
# Also, a t1 distribution has such heavy tails that the variance is infinite and such
# outliers are bound to happen.
# All in all, the samples are too small to perform bootstrap on


""" Question 2 """

df2 = pd.read_csv("Q2.csv")

###Q2.1