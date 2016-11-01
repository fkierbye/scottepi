# scottepi

The scottepi project puts my scotte (v4.99) pelletsburner on the Internet with Raspberry Pi.

Installation:

raspbian packages:
```
sudo apt install wiringpi mc sl python2 flask 
```

crontab:
```
# m h  dom mon dow   command
@reboot /home/frederik/scottepi/reboot.sh >> /home/pi/rebootlog.txt 2>&1
7,37 * * * * /home/frederik/scottepi/ScotteLogger/getweatherdata.py >> /home/pi/weatherlog.txt 2>&1
* * * * * /home/frederik/scottepi/ScotteLogger/getsystemdata.py >> /home/pi/systemlog.txt 2>&1
* * * * * /home/frederik/scottepi/ScotteLogger/getscottedata.py >> /home/pi/scottelog.txt 2>&1
* * * * * /home/frederik/scottepi/ScotteLogger/publisher.sh >> /home/pi/publishlog.txt 2>&1
```

Note: openweathermap has more connection errors when polling at :00 and :30, so we use a small offset
