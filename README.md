# Cell-Data
A project that explores individual choices on use of cellphones or landline phones over 1993-2010.  I find that a multinomial logit is appropriate in exploring the individual choice of 
* Owning a cellphone only 
* Owning a landline only 
* Owning both modes

The exogenous (Right-hand side) variables include 
* Family size
* Real income 
* Gender
* Age 
* Year
* If the subject has a college degree
* If the subject is married
* If the subject lives in an urban area
* If the subject is caucasian 

REQUIRED PACKAGES
Pandas
NumPy
R

INSTRUCTIONS
1. Execute CellDataCleaner.py this will generate the appropriate categories for the endogenous variable on Cell.dta.  The result will be saved as CellDataCleaned.csv
2. Execute CallDataAnalysis.py to fit a multinomial logit to the data.  The results will be in output.txt and associated plot will be in Rplots.pdf
