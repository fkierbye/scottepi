#!/usr/bin/python
import requests
import json
from pprint import pprint
import subprocess
import serial
import datetime
import time

timestamp = ((int(time.time())/60)*60) # round to nearest minute
#date = datetime.datetime.now()
#print (date.strftime("%Y-%m-%d %H:%M"))

project_path="/home/frederik/scottepi/ScotteLogger/"
rrd_db_file=project_path+"scotte.rrd"
json_file=project_path+"scottedata.json"

# get data from serial port
ser = serial.Serial ("/dev/ttyUSB0")
ser.baudrate = 9600
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.bytesize=serial.EIGHTBITS
ser.timeout=3 #seconds
dataOut="Z000000Z"
ser.write(dataOut)
dataIn = ser.read(500)
ser.close()

#remove last checksum character TODO: check if it is correct!
dataIn = dataIn[:-1]

# split data into list
dataList = dataIn.split()

#print dataList

# update rrd database
# luckily somebody created the rrd database to be exactly the same as the output
rrd_values=str(timestamp)
for val in dataList:
    rrd_values+=":"
    rrd_values+=str(val)

print(rrd_values)
retval = subprocess.call(['/usr/bin/rrdtool', 'update', rrd_db_file, rrd_values])
#print("rrdtool returnvalue:" + str(retval))

# create new dictionary with my values
myscottedata = {}
myscottedata['ydelse'] = int(dataList[0])
myscottedata['effekt'] = int(dataList[1])
myscottedata['kedel_temp'] = int(dataList[2])/float(10) # divide by 10 to get correct value
myscottedata['skakt_temp'] = int(dataList[3])
myscottedata['roeg_temp'] = int(dataList[4])
myscottedata['ilt'] = int(dataList[5])
myscottedata['lys'] = int(dataList[6])
myscottedata['snegl_sec'] = int(dataList[7])
myscottedata['el_sec'] = int(dataList[8])
myscottedata['alarm'] = int(dataList[9])
myscottedata['ref_kedel_temp'] = int(dataList[10])
myscottedata['ref_ilt'] = int(dataList[11])
myscottedata['kapacitet'] = int(dataList[12])
myscottedata['skorsten'] = int(dataList[13])
myscottedata['maetning_lav'] = int(dataList[14])
myscottedata['maetning_hoej'] = int(dataList[15])
myscottedata['tilstand'] = int(dataList[16])
myscottedata['spare'] = int(dataList[17])

#translate tilstand to text
if myscottedata['tilstand'] == 2:
    myscottedata['tilstand_text'] = "opstart"
elif myscottedata['tilstand'] == 5:
    myscottedata['tilstand_text'] = "drift"
elif myscottedata['tilstand'] == 9:
    myscottedata['tilstand_text'] = "pause"
elif myscottedata['tilstand'] == 13:
    myscottedata['tilstand_text'] = "fejl"
elif myscottedata['tilstand'] == 14:
    myscottedata['tilstand_text'] = "slukket"
else:
    myscottedata['tilstand_text'] = "? ("+str(myscottedata['tilstand'])+")"

# export data to json file
with open(json_file, 'w') as outfile:
    json.dump(myscottedata, outfile, sort_keys=True, indent=4, separators=(',', ': '))
