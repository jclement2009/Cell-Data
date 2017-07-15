#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:29:04 2017

@author: Joseph
"""

import base64
import pandas as pd
import statsmodels.api as sm
import numpy as np
import os
import io

#Custom function for calling a csv file
def callcsv(csvname):
    csvname1 = str(csvname) + ".csv"
    csvfilename = os.path.abspath(os.path.join(csvname1))
    return csvfilename
    
#Custom function that will take csv file name and convert it directly into a dataframe
def createdf(name):
    stuff = callcsv(name)
    converter = pd.read_csv(stuff)
    df = pd.DataFrame(converter)
    return df

df = createdf('CellDataCleaned')

#Defining X variables
X = df.loc[:, lambda df: ['fam_size', 'rinc', 'college', 'married', 'urban', 'male', 'white', 'age_ref', 'year']]

#Adding a constant term
X = sm.add_constant(X, prepend = False)

#Defining Y variables
Y = df['choice']

#Defining the logit model
logit = sm.MNLogit(Y, X)

# fit the model
result = logit.fit()

print(result.summary())

