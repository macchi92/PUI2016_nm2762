
# coding: utf-8

# In[71]:

import os
import pandas as pd
import matplotlib as plt
get_ipython().magic('matplotlib inline')


# In[26]:

"/gws/open/NYCOpenData/nycopendata/data" in os.environ.get('DFDATA') 


# In[54]:

PATH = os.getenv('DFDATA')
PATH


# In[52]:

df = pd.read_csv("https://data.cityofnewyork.us/resource/5gde-fmj3.csv")


# In[66]:

df_1 = df[['BBL','Zip']]


# In[72]:

df_1.plot()

