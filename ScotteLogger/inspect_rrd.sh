#!/bin/bash

echo -en "date now   : "
date
echo "::scotte::"
echo -en "last update: "
rrdtool info scotte.rrd  | grep last_update  | cut -d " " -f3 | xargs -0 -I % date -d@% && date
rrdtool info scotte.rrd  | grep last_ds

echo -en "date now   : "
date
echo "::vejr::"
echo -en "last update: "
rrdtool info vejr.rrd  | grep last_update  | cut -d " " -f3 | xargs -0 -I % date -d@% && date
rrdtool info vejr.rrd  | grep last_ds