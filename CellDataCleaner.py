#!/usr/bin/env python3
#!/usr/local/bin/Rscript
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:48:52 2017

@author: Joseph
"""

import pandas as pd
import numpy as np
import os




#Custom function for calling a dta file
def calldta(dtaname):
    dtaname1 = str(dtaname) + ".dta"
    dtafilename = os.path.abspath(os.path.join(dtaname1))
    return dtafilename 
  
df = pd.read_stata(calldta('cell'))

celldf = pd.DataFrame(df)

rowcount = len(celldf['newid'])

celldf["choice"] = pd.Series(np.zeros(rowcount), index=celldf.index)

#Generating the endogenous vector of choices into strings
for pointer in range(0, rowcount, 1): 
    if (celldf.ix[pointer, 'cell'] == 0) & (celldf.ix[pointer, 'land'] == 0):
        celldf.ix[pointer, "choice"] = "Neither"
    if (celldf.ix[pointer, 'cell'] == 1) & (celldf.ix[pointer, 'land'] == 1):
        celldf.ix[pointer, "choice"] = "Both"
    if (celldf.ix[pointer, 'cell'] == 1) & (celldf.ix[pointer, 'land'] == 0):
        celldf.ix[pointer, "choice"] = "Cell Only"
    if (celldf.ix[pointer, 'cell'] == 0) & (celldf.ix[pointer, 'land'] == 1):
        celldf.ix[pointer, "choice"] = "Landline Only"
    percent_comp = ((pointer+1)/rowcount)*100
    print(str(pointer+1) + " of " + str(rowcount) + "; " + str(int(percent_comp)) + " percent complete")

#Dropping all rows with the neither choice
celldf = celldf[celldf.choice != "Neither"]    
  
print("Cleaned csv saved as CellDataCleaned.csv")
celldf.to_csv("CellDataCleaned.csv")

