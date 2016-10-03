
# coding: utf-8

# In[194]:

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


# In[195]:

def getCitiBikeCSV(datestring):
    print ("Downloading", datestring)
    ### First I will heck that it is not already there
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv"):
        if os.path.isfile(datestring + "-citibike-tripdata.csv"):
            # if in the current dir just move it
            if os.system("mv " + datestring + "-citibike-tripdata.csv " + os.getenv("PUIDATA")):
                print ("Error moving file!, Please check!")
        #otherwise start looking for the zip file
        else:
            if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip"):
                if not os.path.isfile(datestring + "-citibike-tripdata.zip"):
                    os.system("curl -O https://s3.amazonaws.com/tripdata/" + datestring + "-citibike-tripdata.zip")
                ###  To move it I use the os.system() functions to run bash commands with arguments
                os.system("mv " + datestring + "-citibike-tripdata.zip " + os.getenv("PUIDATA"))
            ### unzip the csv 
            os.system("unzip " + os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip")
            ## NOTE: old csv citibike data had a different name structure. 
            if '2014' in datestring:
                os.system("mv " + datestring[:4] + '-' +  datestring[4:] + 
                          "\ -\ Citi\ Bike\ trip\ data.csv " + datestring + "-citibike-tripdata.csv")
            os.system("mv " + datestring + "-citibike-tripdata.csv " + os.getenv("PUIDATA"))
    ### One final check:
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")


# In[196]:

getCitiBikeCSV('201505')
getCitiBikeCSV('201506')
getCitiBikeCSV('201507')
getCitiBikeCSV('201508')


# In[197]:

data_2015_05 = pd.read_csv('/home/cusp/nm2762/PUIdata/201505-citibike-tripdata.csv')
data_2015_06 = pd.read_csv('/home/cusp/nm2762/PUIdata/201506-citibike-tripdata.csv')
data_2015_07 = pd.read_csv('/home/cusp/nm2762/PUIdata/201507-citibike-tripdata.csv')
data_2015_08 = pd.read_csv('/home/cusp/nm2762/PUIdata/201508-citibike-tripdata.csv')


# In[198]:

frames = [data_2015_05, data_2015_06, data_2015_07, data_2015_08]
results = pd.concat(frames)
results = results.reset_index(drop=True)
results


# # test female male age distribution

# In[199]:

new_mf_a = results.drop (['tripduration', 'starttime', 'stoptime', 'start station id',
       'start station name', 'start station latitude',
       'start station longitude', 'end station id', 'end station name',
       'end station latitude', 'end station longitude', 'bikeid'], axis=1)

new_mf_a = new_mf_a[new_mf_a['gender'] != 0]

new_mf_a['ageM'] = 2015 - new_mf_a['birth year'][(new_mf_a['usertype'] == 'Subscriber') & (new_mf_a['gender'] == 1)]
new_mf_a['ageF'] = 2015 - new_mf_a['birth year'][(new_mf_a['usertype'] == 'Subscriber') & (new_mf_a['gender'] == 2)]

new_mf_a['ageM'].dropna(inplace=True)
new_mf_a['ageF'].dropna(inplace=True)


# In[200]:

bins = np.arange(10, 99, 5)

axM = new_mf_a.ageM.groupby(pd.cut(new_mf_a.ageM, bins)).agg([count_nonzero]).plot(kind='bar',                                                                 legend=False)
axM.set_title("male riders")

axF = new_mf_a.ageF.groupby(pd.cut(new_mf_a.ageF, bins)).agg([count_nonzero]).plot(kind='bar',                                                                legend=False)
axF.set_title("female riders")


# In[201]:

csM=new_mf_a.ageM.groupby(pd.cut(new_mf_a.ageM, bins)).agg([count_nonzero]).cumsum()

csF=new_mf_a.ageF.groupby(pd.cut(new_mf_a.ageF, bins)).agg([count_nonzero]).cumsum()

print (np.abs(csM / csM.max()-csF / csF.max()))

pl.plot(bins[:-1] + 5, csM / csM.max(), label = "M")
pl.plot(bins[:-1] + 5, csF / csF.max(), label = "F")
pl.plot(bins[:-1] + 5, np.sqrt(csF / csF.max() - csM / csM.max())**2, 'k-',
        label = "difference")
pl.xlabel("Age")
pl.ylabel("Normalized Cumulative Number")
pl.legend()



# In[202]:

import scipy.stats


# # First test 

# In[203]:

ks = scipy.stats.ks_2samp(new_mf_a.ageM, new_mf_a.ageF)
print (ks)


# In[204]:

datamale = new_mf_a[new_mf_a['gender'] == 1]
datafemale = new_mf_a[new_mf_a['gender'] == 2]


datamale.drop(['ageF'], axis=1, inplace=True)
datafemale.drop(['ageM'], axis=1, inplace=True)

datamale['ageM'].dropna(inplace= True)
datafemale['ageF'].dropna(inplace= True)

damale = datamale.reset_index(drop=True)
datafemale = datafemale.reset_index(drop=True)

oneeach200male = datamale.iloc[::200,:]
oneeach200female = datafemale.iloc[::200,:]

ks = scipy.stats.ks_2samp(oneeach200male.ageM, oneeach200female.ageF)
print (ks)


# # Second test

# In[205]:

datamalerisize = datamale.iloc[:827770]
scipy.stats.pearsonr(datamalerisize.ageM, datafemale.ageF)


# # Third test
# 

# In[206]:

scipy.stats.spearmanr(datamalerisize.ageM, datafemale.ageF)


# # Day and Night age Distribution

# In[207]:

new_dn_a = results.drop (['tripduration', 'start station id',
       'start station name', 'start station latitude',
       'start station longitude', 'stoptime', 'end station id', 'end station name',
       'end station latitude', 'end station longitude', 'bikeid', 'gender'], axis=1)


new_dn_a = new_dn_a[new_dn_a['usertype'] == 'Subscriber']


#new_dn_a
#new_dn_a = new_dn_a[new_dn_a['usertype'] == 'Subriber']


# In[208]:

new_dn_a.drop(['usertype'], axis=1, inplace=True)


# # DEFINE DAY-TRIP AS ALL THE TRIP STARTING BETWEEN 6.AM AND 6.PM.  
# 

# # DEFINE NIGHT-TRIP AS ALL THE TRIP STARTING BETWEEN 6.PM AND 6.AM

# In[209]:

new_dn_a = new_dn_a.reset_index(drop=True)
new_dn_a['ageM'] = 2015 - new_dn_a['birth year']
new_dn_a


# In[210]:

new_dn_a['ageM'] = 2015 - new_dn_a['birth year']
new_dn_a.drop(['birth year'], axis=1, inplace=True)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



