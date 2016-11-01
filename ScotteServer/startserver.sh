#!/bin/bash

#define scotte home dir, use absolute paths when running from cronjob
project_path="/home/frederik/scottepi/ScotteServer"

# get time and date
ymdhm=`date +'%Y-%m-%d %H:%M'`
echo -en "Started server at: "
echo "$ymdhm" 

cd $project_path
/usr/bin/python app.py > /dev/null