# -*- coding: utf-8 -*-
# Author: Jing Chen @ EMC Corp. jing.chen2@emc.com
#

from WindowsWifiDistance import get_distance
from Trilateration import Trilateration
import time

ap00 = {}
ap00.update({"name":"AP00", "SSID":"dlink_c2", "xpos":1, "ypos":1})
ap01 = {}
ap01.update({"name":"AP01", "SSID":"dlink_5d", "xpos":801, "ypos":1})
ap10 = {}
ap10.update({"name":"AP10", "SSID":"dlink_11", "xpos":1, "ypos":401})

ap00_result = get_distance(ap00["SSID"], -100)
ap01_result = get_distance(ap01["SSID"], -100)
ap10_result = get_distance(ap10["SSID"], -100)

my_location = Trilateration(ap00["xpos"],ap00["ypos"],ap00_result['distance'],\
                            ap01["xpos"],ap01["ypos"],ap01_result['distance'],\
                            ap10["xpos"],ap10["ypos"],ap10_result['distance'])

print "Found my location is: ", my_location

ap00.update({"distance in centimeter": ap00_result["distance"]})
ap00.update({"signal quality in percentage": ap00_result["quality"]})
ap00.update({"signal strength in dBm": ap00_result["strength"]})
ap00.update({"time_stamp": time.ctime() })

ap01.update({"distance in centimeter": ap01_result["distance"]})
ap01.update({"signal quality in percentage": ap01_result["quality"]})
ap01.update({"signal strength in dBm": ap01_result["strength"]})
ap01.update({"time_stamp": time.ctime() })

ap10.update({"distance in centimeter": ap10_result["distance"]})
ap10.update({"signal quality in percentage": ap10_result["quality"]})
ap10.update({"signal strength in dBm": ap10_result["strength"]})
ap10.update({"time_stamp": time.ctime() })


print ap00
print ap01
print ap10

import json
with open('Distances.json', 'w') as outfile:
    json.dump(ap00, outfile)
    json.dump(ap01, outfile)
    json.dump(ap10, outfile)

