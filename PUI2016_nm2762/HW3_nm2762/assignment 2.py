
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



get_ipython().magic('pylab inline')


get_ipython().system("curl -O 'https://s3.amazonaws.com/tripdata/201402-citibike-tripdata.zip'")

zf = zp.ZipFile('201402-citibike-tripdata.zip')
zf.extractall()
zf.close()




# In[2]:

zf = zp.ZipFile('201402-citibike-tripdata.zip')
zf.extractall()
zf.close()


# In[3]:

data = pd.read_csv('2014-02 - Citi Bike trip data.csv')
data


# In[4]:

print ('We have the data of the city bike trip of February 2014')
print ('')
print (' HYPOTHESIS ')
print (' The average number of bike-trips of a working day in February')
print (' is higher than the average numbers of bike trips in the weekend')
print ('')
print (' Lets define')
print (' WORKING DAY = MONDAY-FRIDAY ')
print (' WEEK-END = SATURDAY AND SUNDAY')
print (' BIKE TRIP = A pick up of a bike')
print (' AVERAGE NUMBER OF BIKE-TRIPS = Total number of bike-trips of "n" days divided by "n"')
print ('')
print ('')
print (' NULL HYPOTHESIS')
print (' The average number of bike-trips of a working day in February')
print (' is equal or less than the average numbers of bike trips in the weekend ')

print ('')
print ('Significance level a=0.05')


# In[5]:

data.columns


# In[6]:

data['date'] = pd.to_datetime(data['starttime'])

data.drop(['tripduration', 'starttime', 'stoptime', 'start station id',
       'start station name', 'start station latitude',
       'start station longitude', 'end station id', 'end station name',
       'end station latitude', 'end station longitude', 'bikeid', 'usertype',
       'birth year', 'gender'], axis=1, inplace=True)



# In[7]:

data


# In[8]:

print (' We know that the 01 February 2014 was Saturday')


# In[9]:

data ['weekday'] = data ['date'].apply(lambda x: x.weekday())


# In[10]:

data


# In[11]:

norm_w = 1 
ax = ((data['date'].groupby([data['date'].dt.weekday]).count()) / norm_w).plot(kind="bar", color='IndianRed', alpha=0.5)

tmp = ax.xaxis.set_ticklabels(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], fontsize=20)


# In[12]:

data_count = data.groupby('weekday').size()

working_day_trip = 0
weekend_day_trip = 0

for i in range(0 , 4):
    working_day_trip = data_count[i] + working_day_trip

for i in (5,6):
    weekend_day_trip = data_count[i] + weekend_day_trip
    
print (weekend_day_trip)
print (working_day_trip)


# In[13]:

average_weekend_day_trip = weekend_day_trip / 8
average_working_day_trip = working_day_trip / 20


# In[14]:

print (average_weekend_day_trip)
print (average_working_day_trip)


# In[15]:

array = [average_weekend_day_trip , average_working_day_trip]
array 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



