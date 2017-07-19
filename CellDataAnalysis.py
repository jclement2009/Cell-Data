#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:29:04 2017

@author: Joseph
"""

import os
import subprocess 

#Finding Rscript
def findRscript():
    for root, dirs, files in os.walk(os.path.abspath(os.sep)):
        for name in files:
            if "bin" in os.path.abspath(os.path.join(root, name)):
                if name == "Rscript":
                    return os.path.abspath(os.path.join(root, name)) 
                    

#Executing R Script
print("Executing CellDataAnalysisR.R. \nThis may take a minute or 2. \n******")
subprocess.call([findRscript(), "--vanilla", os.path.abspath(os.path.join("CellDataAnalysisR.R"))])
print("***Analysis Complete***")
print("Regression Results: \nSEE Ouput.txt")
print("Graphical Results: \nSEE Rplots.pdf")