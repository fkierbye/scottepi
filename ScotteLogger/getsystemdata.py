#!/usr/bin/python
import subprocess
import os
import json
from pprint import pprint

project_path="/home/scotte/scottepi/ScotteLogger/"
json_file=project_path+"systemdata.json"

def get_mem_usage():
    """Returns memory usage in percent, see http://www.linuxatemyram.com/ for available ram"""
    try:
        s = subprocess.check_output(["free","-m"])
        lines = s.split('\n') 
        mem_total=float(lines[1].split()[1])
        mem_free=int(lines[2].split()[3])
        mem_used=mem_total-mem_free
        mem_percent_used=int(round(mem_used*100/mem_total))
        return ( mem_percent_used )
    except:
        return 0

def get_disk_usage():
    """Returns disk usage in percent"""
    try:
        s = subprocess.check_output(["df","-m"])
        lines = s.split('\n') 
        disk_total=float(lines[1].split()[1])
        disk_free=int(lines[1].split()[3])
        disk_used=disk_total-disk_free
        disk_percent_used=int(round(disk_used*100/disk_total))
        return ( disk_percent_used )
    except:
        return 0

def get_process_count():
    """Returns the number of processes"""
    try:
        s = subprocess.check_output(["ps","-e"])
        return len(s.split('\n')) 
    except:
        return 0

def get_uptime():
    """Returns uptime as a string (tbd tuple? )"""
    try:
        s = subprocess.check_output(["uptime"])
        load_split = s.split('load average: ')
        up = load_split[0]
        up_pos = up.rfind(',',0,len(up)-4)
        up = up[:up_pos].split('up ')[1]
        return ( up ) 
    except:
        return ( "" )

def get_cpu_load_average():
    """Returns a tuple (1 min load, 5 min load, 15 min load )"""
    try:
        s = subprocess.check_output(["uptime"])
        load_split = s.split('load average: ')
        load_1 = float(load_split[1].split(',')[0])
        load_5 = float(load_split[1].split(',')[1])
        load_15 = float(load_split[1].split(',')[2])
        return (load_1, load_5, load_15) 
    except:
        return ( 0, 0, 0 )

def get_ipconnections():
    """Returns the number of network connections"""
    try:
        s = subprocess.check_output(["netstat","-tun"])
        return len([x for x in s.split() if x == 'ESTABLISHED'])
    except:
        return 0

def get_cpu_temperature():
    """Returns the temperature in degrees C"""
    try:
        s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
        return float(s.split('=')[1][:-3])
    except:
        return 0

def get_ipaddress():
    """Returns the current IP address"""
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]
    return ipaddr

def get_cpu_speed():
    """Returns the current CPU speed"""
    s = subprocess.check_output(["/opt/vc/bin/vcgencmd", "get_config", "arm_freq"])
    return int(s.split('=')[1])

def get_wireless_info():
    """Returns a touple with ssid and quality in %"""
    try:
        s = subprocess.check_output(["wavemon","-iwlan0","-d"])
        lines = s.split('\n') 
        ssid = lines[5].split()[1].strip("\"")
        quality_str = lines[18].split()[2]
        quality = int(quality_str.split('/')[0])
        quality_max = float(quality_str.split('/')[1]) # make a float to calculate floating point factor below
        factor = 100/quality_max
        quality_percent = int(round(quality*factor)) # make in % usually max is 70 
        return ( ssid, quality_percent )
    except:
        return ("", 0)

systeminfo = {}
systeminfo['mem_usage'] = get_mem_usage()
systeminfo['disk_usage'] = get_disk_usage()
systeminfo['process_count'] = get_process_count()
systeminfo['cpu_load'] = get_cpu_load_average()
systeminfo['uptime'] = get_uptime()
systeminfo['cpu_temperature'] = get_cpu_temperature()
systeminfo['cpu_speed'] = get_cpu_speed()
systeminfo['ip_address'] = get_ipaddress()
systeminfo['ip_connections'] = get_ipconnections()
systeminfo['wireless_info'] = get_wireless_info()

# export data to json file
with open(json_file, 'w') as outfile:
    json.dump(systeminfo, outfile, sort_keys=True, indent=4, separators=(',', ': '))

pprint( systeminfo)