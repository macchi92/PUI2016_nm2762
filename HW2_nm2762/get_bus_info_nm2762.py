
# coding: utf-8

# In[58]:

import json
import urllib as ulr
import os
import csv
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']

with open (sys.argv[3],'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    for i in range (0, num):
        Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']        [i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']        [i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stopname = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']        ['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopstatus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']        ['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        writer.writerow([Latitude,Longitude,stopname,stopstatus])

   

