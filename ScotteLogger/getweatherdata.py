#!/usr/bin/python
import requests
import json
from pprint import pprint
import datetime
import subprocess
import datetime
import time

timestamp = ((int(time.time())/1800)*1800) # round to nearest half hour
#date = datetime.datetime.now()
#print (date.strftime("%Y-%m-%d %H:%M"))

project_path="/home/scotte/scottepi/ScotteLogger/"
rrd_db_file=project_path+"vejr.rrd"
json_file=project_path+"weatherdata.json"

# From http://openweathermap.org/appid :
#
# How to get accurate API response
# 1 Do not send requests more then 1 time per 10 minutes from one device/one API key. Normally the weather is not changing so frequently.
# 2 Use the name of the server as api.openweathermap.org. Please never use the IP address of the server.
# 3 Call API by city ID instead of city name, city coordinates or zip code. In this case you get precise respond exactly for your city.
# 4 Free account has limitation of capacity and data availability. If you do not get respond from server do not try to repeat your request immediately, but only after 10 min. Also we recommend to store your previous request data.

weather_url="http://api.openweathermap.org/data/2.5/weather?q=Vemb,Denmark&units=metric&appid=389394247425a4b98054f0688ecd14c1"
iconurl = "http://openweathermap.org/img/w/"

retries = 0

while True:
    r = requests.get(weather_url)

    if (r.status_code == 200) and (r.headers['content-type'] == "application/json; charset=utf-8") and (r.encoding == "utf-8"):
        #alternative way openweatherjsondata = json.loads(r.text)
        openweatherjsondata = r.json()

        #pprint(openweatherjsondata)

        #new dictionary for storing weather data in own format
        myweatherdata = {}
        myweatherdata['description'] = str(openweatherjsondata["weather"][0]["description"])
        myweatherdata['icon'] = str(openweatherjsondata["weather"][0]["icon"])
        myweatherdata['iconurl'] = iconurl+str(openweatherjsondata["weather"][0]["icon"])+".png"
        myweatherdata['temperature'] = int(round(openweatherjsondata["main"]["temp"]))
        myweatherdata['windspeed'] = int(round(openweatherjsondata["wind"]["speed"]))
        myweatherdata['winddirection'] = int(round(openweatherjsondata["wind"]["deg"]))
        myweatherdata['humidity'] = int(round(openweatherjsondata["main"]["humidity"]))
        myweatherdata['pressure'] = int(round(openweatherjsondata["main"]["pressure"]))
    
        #convert unix timestamps to iso8601
        sunrise_unix = openweatherjsondata["sys"]["sunrise"]
        sunset_unix = openweatherjsondata["sys"]["sunset"]
        sunrise_iso8601 = datetime.datetime.fromtimestamp(int(sunrise_unix)).strftime('%H:%M')
        sunset_iso8601 = datetime.datetime.fromtimestamp(int(sunset_unix)).strftime('%H:%M')
        #sunset_iso8601 = datetime.datetime.fromtimestamp(int(sunset_unix)).strftime('%Y-%m-%d %H:%M:%S')
    
        myweatherdata['sunrise'] = str(sunrise_iso8601)
        myweatherdata['sunset'] = str(sunset_iso8601)
        #pprint (myweatherdata)

        # update rrd database,
        rrd_values = str(timestamp)+":"
        rrd_values += "20:" # fake indoor temp to 20
        rrd_values += str(myweatherdata['temperature'])+":"
        rrd_values += str(myweatherdata['humidity'])+":"
        rrd_values += str(myweatherdata['pressure'])+":"
        rrd_values += str(myweatherdata['winddirection'])+":"
        rrd_values += str(myweatherdata['windspeed'])

        print(rrd_values)
        retval = subprocess.call(['/usr/bin/rrdtool', 'update', rrd_db_file, rrd_values])
        #print("rrdtool returnvalue:" + str(retval))

        # translate degrees to compass
        if myweatherdata['winddirection'] >= 23 and myweatherdata['winddirection'] < 68:
            myweatherdata['winddirection_text'] = "NE"
        elif myweatherdata['winddirection'] >= 68 and myweatherdata['winddirection'] < 113:
            myweatherdata['winddirection_text'] = "E"
        elif myweatherdata['winddirection'] >= 113 and myweatherdata['winddirection'] < 158:
            myweatherdata['winddirection_text'] = "SE"
        elif myweatherdata['winddirection'] >= 158 and myweatherdata['winddirection'] < 203:
            myweatherdata['winddirection_text'] = "S"
        elif myweatherdata['winddirection'] >= 203 and myweatherdata['winddirection'] < 248:
            myweatherdata['winddirection_text'] = "SW"
        elif myweatherdata['winddirection'] >= 248 and myweatherdata['winddirection'] < 293:
            myweatherdata['winddirection_text'] = "W"
        elif myweatherdata['winddirection'] >= 293 and myweatherdata['winddirection'] < 338:
            myweatherdata['winddirection_text'] = "NW"
        else:
            myweatherdata['winddirection_text'] = "N"

        # export data to json file
        with open(json_file, 'w') as outfile:
            json.dump(myweatherdata, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        break

    else:
	retries+=1
	if(retries < 3):
            print("error: "+str(retries))
            print(r.text)
            print("expected: status: 200, headers: application/json; charset=utf-8, encoding: utf-8")
	    print("got     : status: "+str(r.status_code)+", headers: "+r.headers['content-type']+", encoding: "+ r.encoding)
	    print("trying again in 42 seconds")
	    time.sleep(42) #sleep 42 seconds
	else:
	    print("retry max giving up...")
	    break
