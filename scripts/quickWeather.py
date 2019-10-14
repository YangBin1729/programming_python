#!python3
# quickWeather.py - Prints the Weather for a location from the command line.

import json
import sys
import requests

if len(sys.argv) < 2:
    print('Usage:quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathremap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location
res =  requests.get(url)
res.raise_for_status()

weatherData = json.loads(res.text)

