
# coding: utf-8

# ### H0: the commute time is the same or longer with the new bus route as it was before (New mean => Old mean)
# ### Ha: the commute time with the new bus route is measurable shorter than it was before (New mean < Old mean)
# ### Confidence level: alpha = 0.05
# ### Old mean = 36

# In[25]:

import numpy as np
import matplotlib as pt
import pandas as pd


# In[28]:

newBusData = pd.read_csv('times.txt', header = None)


# In[29]:

newBusData.head()


# In[42]:

oldMean = 36
newMean = newBusData.mean()
sigma = 6
N = newBusData.count()


# In[43]:

print "Mean for new route: %.2f" %newMean
print "Standard deviation for new route: %.2f" %newBusData.std()


# In[44]:

Z_test = (oldMean - newMean)/(sigma / np.sqrt(N))


# In[45]:

print "Outcome of the z test: %.2f" %Z_test


# ### The result of the z test is 2.56, meaning our new mean is further than two standard deviations away
# ### from the old mean. We can therefor reject the null hypothesis with the confidence level stated above
# ### as 95% of measurments will lie with inside 2 standard deviation from the mean.
