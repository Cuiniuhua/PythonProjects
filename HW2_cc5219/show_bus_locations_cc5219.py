
from __future__ import print_function
import requests
import json
import urllib.request as ulr
import os
import sys
import numpy as np
key=sys.argv[1]
bus_line=sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef="+ busline
requrl = requests.get(url)
data=requrl.json()
buses= data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
numbus=np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print ("Bus Line: %s"%(bus_line))
print ("Number of Active Buses: %d" %(activebus))
for i in range(len(buses)):
        lattd = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lontd = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus %s is at latitude %s and longtitude %s" %(i+1,lattd,lontd))
