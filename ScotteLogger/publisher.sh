#!/bin/bash

#define scotte home dir, use absolute paths when running from cronjob
project_path="/home/scotte/scottepi/ScotteLogger/"

#define dir where html and graph images should be published
publish_path="/home/scotte/scottepi/ScotteServer/static/"

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

