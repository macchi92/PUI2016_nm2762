
# coding: utf-8

# In[77]:

import os
import pandas as pd
import matplotlib as plt
get_ipython().magic('matplotlib inline')


# In[78]:

"/gws/open/NYCOpenData/nycopendata/data" in os.environ.get('DFDATA') 


# In[79]:

PATH = os.getenv('DFDATA')
PATH


# In[83]:

df = pd.read_csv(PATH +'/5gde-fmj3/1414246119/5gde-fmj3')


# In[84]:

df_1 = df[['BBL','Zip']]


# In[85]:

df_1.plot()


# In[ ]:



