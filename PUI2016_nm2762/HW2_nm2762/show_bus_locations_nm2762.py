import json
import urllib as ulr
import os
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation'].keys()

print 'Bus Line :' , sys.argv[2]

print ('Number of Active Buses : %d' %num)
for i in range (0, num):
    Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
    [i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
    [i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus number %d is at Latitude %f and Longitude %f' %(i,Longitude,Latitude))





