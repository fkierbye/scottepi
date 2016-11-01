#!/bin/bash

#define scotte home dir, use absolute paths when running from cronjob
project_path="/home/frederik/scottepi/ScotteLogger/"

#define dir where html and graph images should be published
publish_path="/home/pi/software/ScotteServer/static/"

# get time and date
ymdhm=`date +'%y-%m-%d %H:%M'`
echo "$ymdhm"

# wait for data collection
sleep 10

# create graph images (png format)
${project_path}/rrd_graph_create.sh

# copy graph images to where it should be published
for filename in *.png; do
  cp -v ${project_path}/$filename ${publish_path}
done

# copy json data to where it should be published
for filename in *.json; do
  cp -v ${project_path}/$filename ${publish_path}
done

