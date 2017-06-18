#Import Required Libarys and modules
import sys
import json
import urllib2
from email.mime.text import MIMEText
from subprocess import Popen, PIPE


#Check arguments passed in command line
try:
    city = sys.argv[1]
    email = sys.argv[2]
except IndexError:
    print 'Value missing run as "WeatherReport.py [City] [Email Address]"'
else:
    #Check URL for API is working.
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
        #Email current weather
        weather_object = json.load(weathersource)
        current_weather =  weather_object['weather'][0]['description']
        msg = MIMEText("The Weather Is "  + current_weather + "for " + city)
        msg["From"] = "me@jneil.online"
        msg["To"] = email
        msg["Subject"] = "Your weather report."
        p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
        p.communicate(msg.as_string())







