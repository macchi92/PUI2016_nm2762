
# coding: utf-8

# In[1]:

from __future__  import print_function, division
import pylab as pl
import pandas as pd
import numpy as np
import os as os
import zipfile as zp
import csv as csv
import urllib as ulr
from pandas import DataFrame


get_ipython().magic('pylab inline')




# In[27]:

tab_chistat = [[0.1 * 568, 0.9 * 568], [0.117 * 409, 0.883 * 409]]
product_total = 104.653*872.347*568*409


for i in (0, 1):
    for j in (0, 1):
        print (tab_chistat[i][j])
        


|convicted of a fellony     |     yes   | no        |                  
|---------------------------|-----------|-----------|----------------|
| test sample               |  56.8     |   511.2   |     568        |
| control sample            |  47.853   |   361.147 |    409         |
|                           |           |           |                |
| total                     |  104,653  |   872,347 |    977.0       |
# In[34]:

TotalN = 0

for i in (0, 1):
    for j in (0, 1):
        TotalN = TotalN + tab_chistat[i][j]

chistat = ((tab_chistat[0][0]*tab_chistat[1][1]-tab_chistat[0][1]*tab_chistat[1][0])**2) * TotalN / product_total
print ('The chi square is'), chistat


# In[ ]:



