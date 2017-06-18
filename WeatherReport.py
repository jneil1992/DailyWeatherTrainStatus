#Import Required Libarys and modules
import sys
import json
import urllib2


#Check arguments passed in command line
try:
    City = sys.argv[1]
except IndexError:
    print "Value missing run as WeatherReport.py [City]"
else:
    print sys.argv[1]
    try:
        weathersource = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=%city,uk&appid=4bfec0da097701d85c1d0a695079496d')
    except urllib2.HTTPError , err:
        if err.code == 404:
            print "page not found!!"
        elif err.code == 403:
            print "Access denied!"
        else:
            print "Someother HTTP Error recieved", err.code
    except urllib2.URLError, err:
        print "Some Other Error Happened:", err.reason
    else:
        weather_object = json.load(weathersource)
        print weather_object['weather'][0]['description']






