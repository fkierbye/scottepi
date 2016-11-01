#!/bin/bash

rrdtool create scotte.rrd \
            DS:ydelse:GAUGE:60:0:100   \
            DS:effekt:GAUGE:60:0:160  \
            DS:kedel_temp:GAUGE:60:0:1000   \
            DS:skakt_temp:GAUGE:60:0:1000 \
            DS:roeg_temp:GAUGE:60:0:1000   \
            DS:ilt:GAUGE:60:60:1000  \
            DS:lys:GAUGE:60:60:100   \
            DS:snegl_sec:COUNTER:60:0:100000000   \
            DS:el_sec:COUNTER:60:0:100000000  \
            DS:alarm:GAUGE:60:U:U   \
            DS:ref_kedel_temp:GAUGE:60:40:85  \
            DS:ref_ilt:GAUGE:60:0:100   \
            DS:kapacitet:GAUGE:60:0:10000  \
            DS:skorsten:GAUGE:60:0:10   \
            DS:maetning_lav:GAUGE:60:50:1500  \
            DS:maetning_hoej:GAUGE:60:10:1000   \
            DS:tilstand:GAUGE:60:0:100  \
            DS:spare:GAUGE:60:0:100  \
            RRA:AVERAGE:0.5:1:1440      \
            RRA:AVERAGE:0.5:10:1008     \
            RRA:AVERAGE:0.5:60:744     \
            RRA:AVERAGE:0.5:1440:730
# scotte:   sampling freq 60 secs = 1 minute
#           1 day of 1min samples     (1 sample, 60samples/hour x 24h = 1440 samples)
#           1 week of 10 min samples  (10 sample average, 6samples/hour x 24h x 7d = 1008 samples)
#           1 month of 1 hour samples (60 samples average, 1sample/hour x 24h x 31d = 744 samples)
#           2 years of 1 day samples  (1440 sample average, 1 sample/day x 730d = 730 samples)

rrdtool create vejr.rrd  \
            DS:inde_temperatur:GAUGE:1800:0:50   \
            DS:ude_temperatur:GAUGE:1800:-50:50   \
            DS:luftfugtighed:GAUGE:1800:0:100   \
            DS:lufttryk:GAUGE:1800:500:1500 \
            DS:vindretning:GAUGE:1800:0:360 \
            DS:vindhastighed:GAUGE:1800:0:1000 \
            RRA:AVERAGE:0.5:1:1488      \
            RRA:AVERAGE:0.5:48:730
# vejr:     sampling freq 1800 secs = 30 minutes
#           1 month of 30min samples (1 sample, 48samples/day x 31d = 1488 sampels) 
#           2 years of 1 day samples (48 sample average, 1sample/day x 730d = 730 samples)

