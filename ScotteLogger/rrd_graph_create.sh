#!/bin/bash
scotte_path="/home/scotte/scottepi/ScotteLogger/"

rrdtool graph ${scotte_path}/pillefyr1.png --title 'Pillefyr sidste døgn' -l0 -h200 -w500 --start -24h \
               --slope-mode \
               DEF:ydelse=${scotte_path}/scotte.rrd:ydelse:AVERAGE:step=180 \
               DEF:kedeltemp=${scotte_path}/scotte.rrd:kedel_temp:AVERAGE:step=180 \
               DEF:vvbtemp=${scotte_path}/scotte.rrd:roeg_temp:AVERAGE:step=180 \
               CDEF:realkedeltemp=kedeltemp,10,/ \
               LINE2:ydelse#00FF00:"Ydelse (procent)" \
               LINE2:realkedeltemp#FF0000:"Kedel temp (grader)" \
               LINE2:vvbtemp#0000FF:"VVB temp (grader)"

rrdtool graph ${scotte_path}/pillefyr2.png --title 'Pillefyr sidste måned' -l0 -h200 -w500 --start -1m \
               --slope-mode \
               DEF:ydelse=${scotte_path}/scotte.rrd:ydelse:AVERAGE \
               DEF:kedeltemp=${scotte_path}/scotte.rrd:kedel_temp:AVERAGE \
               DEF:vvbtemp=${scotte_path}/scotte.rrd:roeg_temp:AVERAGE \
               CDEF:realkedeltemp=kedeltemp,10,/ \
               LINE2:ydelse#00FF00:"Ydelse (procent)" \
               LINE2:realkedeltemp#FF0000:"Kedel temp (grader)" \
               LINE2:vvbtemp#0000FF:"VVB temp (grader)"

rrdtool graph ${scotte_path}/pillefyr3.png --title 'Pillefyr sidste år'  -l0 -h200 -w1000 --start -1y \
               --slope-mode \
               DEF:ydelse=${scotte_path}/scotte.rrd:ydelse:AVERAGE:step=172800 \
               DEF:kedeltemp=${scotte_path}/scotte.rrd:kedel_temp:AVERAGE:step=172800 \
               DEF:vvbtemp=${scotte_path}/scotte.rrd:roeg_temp:AVERAGE \
               CDEF:realkedeltemp=kedeltemp,10,/ \
               LINE2:ydelse#00FF00:"Ydelse (procent)" \
               LINE2:realkedeltemp#FF0000:"Kedel temperatur (grader)" \
               LINE2:vvbtemp#0000FF:"VVB temperatur (grader)"

rrdtool graph ${scotte_path}/vejr_forbrug1.png --title 'Vejr og forbrug sidste døgn' -l0 -h200 -w500 --start -24h \
               DEF:vindhastighed=${scotte_path}/vejr.rrd:vindhastighed:AVERAGE:step=7200 \
               DEF:ude_temperatur=${scotte_path}/vejr.rrd:ude_temperatur:AVERAGE:step=7200 \
               DEF:forbrug_sec=${scotte_path}/scotte.rrd:snegl_sec:AVERAGE:step=1800\
               CDEF:forbrug_100gram=forbrug_sec,60,*,3.6,* \
               AREA:forbrug_100gram#00FF00:"Pille forbrug (100g)"  \
               LINE2:vindhastighed#FF0000:"Vind (m/s)" \
               LINE2:ude_temperatur#0000FF:"Ude temp. (grader)" 

rrdtool graph ${scotte_path}/vejr_forbrug2.png --title 'Vejr og forbrug sidste måned' -l0 -h200 -w500 --start -1m \
               DEF:vindhastighed=${scotte_path}/vejr.rrd:vindhastighed:AVERAGE:step=10800 \
               DEF:ude_temperatur=${scotte_path}/vejr.rrd:ude_temperatur:AVERAGE:step=10800 \
               DEF:forbrug_sec=${scotte_path}/scotte.rrd:snegl_sec:AVERAGE:step=86400 \
               CDEF:forbrug_kgram=forbrug_sec,311.040,* \
               AREA:forbrug_kgram#00FF00:"Pille forbrug (kg)"  \
               LINE2:vindhastighed#FF0000:"Vind (m/s)" \
               LINE2:ude_temperatur#0000FF:"Ude temp. (grader)" 

rrdtool graph ${scotte_path}/vejr_forbrug3.png --title 'Vejr og forbrug sidste år' -l0 -h200 -w1000 --start -1y \
               DEF:vindhastighed=${scotte_path}/vejr.rrd:vindhastighed:AVERAGE:step=172800 \
               DEF:ude_temperatur=${scotte_path}/vejr.rrd:ude_temperatur:AVERAGE:step=172800 \
               DEF:forbrug_sec=${scotte_path}/scotte.rrd:snegl_sec:AVERAGE:step=86400 \
               CDEF:forbrug_kgram=forbrug_sec,311.040,* \
               AREA:forbrug_kgram#00FF00:"Pille forbrug (kg)"  \
               LINE2:vindhastighed#FF0000:"Vind (m/s)" \
               LINE2:ude_temperatur#0000FF:"Ude temp. (grader)"
