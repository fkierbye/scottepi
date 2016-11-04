#!/usr/bin/python
import os.path
import json
from pprint import pprint

# Modes:
# summer = only start for making hot water, when VVB temperature is below X degrees
# mid season = only start in selected timeslots
# winter = run all the time (except pause), load vvb

project_path="/home/frederik/scottepi/"
scottemanager_json_file=project_path+/ScotteManager/scottemanager.json
scottelog_json_file=project_path+"/ScotteLogger/scottedata.json"

scotte_off_manual_file=project_path+"/ScotteLogger/scotte_off_manual"
scotte_off_timer_file=project_path+"/ScotteLogger/scotte_off_timer"
scotte_off_web_file=project_path+"/ScotteLogger/scotte_off_web"
scotte_summermode_file=project_path+"/ScotteLogger/scotte_off_timer"


scottedata = {}
try:
    with open(scottelog_json_file) as infile:
	scottedata = json.load(infile)
except 

scottemanager = {}
with open(scottelog_json_file) as infile:
    myscottedata = json.load(infile)

scottemanager['mode'] = "vinter"
scottemanager['pump_on'] = True
scottemanager['vvb_on'] = True
scottemanager['scotte_off_timer'] = "None"
scottemanager['scotte_off_manual'] = "None"
scottemanager['scotte_off_manual'] = "None"

# Note we manage this with simple (empty files) as flags so we do not access the same file from more processes.

#assume that everything needs to be on, and make checks below to turn off
scotte = 1
vvb = 1
pump = 1

# check for any override (only read override files here, set from other sources)
if os.path.isfile(ScotteOffTimer)  or os.path.isfile(ScotteOffManual) or os.path.isfile(ScotteOffWeb):
    scotte = 0

#only run pump if fyr is on
if scotte == 1 and myscottedata['tilstand_text'] = "drift" and myscottedata['kedel_temp'] > 50:
    pump = 1

