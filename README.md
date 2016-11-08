# scottepi

The scottepi project puts my scotte (v4.99) pelletsburner on the Internet with Raspberry Pi.

## Installation:
 
### Raspbian packages:
```
sudo apt install mc sl wiringpi git wavemon rrdtool python-flask python-requests python-serial
```

### Crontab:
```
# m h  dom mon dow   command
@reboot /home/scotte/scottepi/rebootman.sh >> /home/scotte/rebootlog.txt 2>&1
7,37 * * * * /home/scotte/scottepi/ScotteLogger/getweatherdata.py >> /home/scotte/weatherlog.txt 2>&1
* * * * * /home/scotte/scottepi/ScotteLogger/getsystemdata.py >> /home/scotte/systemlog.txt 2>&1
* * * * * /home/scotte/scottepi/ScotteLogger/getscottedata.py >> /home/scotte/scottelog.txt 2>&1
* * * * * /home/scotte/scottepi/ScotteLogger/publisher.sh >> /home/scotte/publishlog.txt 2>&1
```
openweathermap has more connection errors when polling at :00 and :30, so we use a small offset

## Pinout: (Model B2)

| Usage      | Peripherals  | Pins  | Peripherals | Usage        |
| ---        | ---          | ---   | ---         | ---          |
| Relay Vcc  | 3.3V         |  1  2 | 5V          | Relay JD-Vcc |
|            | GPIO2/SDA0   |  3  4 | 5V          | HC-SR04 Vcc  | 
|            | GPIO3/SCL0   |  5  6 | GND         |              |
|            | GPIO4        |  7  8 | GPIO14/TXD0 |              |
| Relay GND  | GND          |  9 10 | GPIO15/RXD0 |              |
| Relay 1    | GPIO17       | 11 12 | GPIO18/PWM0 | Relay 2      | 
| Relay 3    | GPIO27       | 13 14 | GND         | HC-SR04 GND  | 
| Relay 4    | GPIO22       | 15 16 | GPIO23      | HC-SR04 TRIG | 
|            | 3.3V         | 17 18 | GPIO24      | HC-SR04 ECHO | 
|            | GPIO10/MOSI0 | 19 20 | GND         |              | 
|            | GPIO9/MISO0  | 21 22 | GPIO25      |              | 
|            | GPIO11/SCLK0 | 23 24 | GPIO8/CE0   |              |
|            | GND          | 25 26 | GPIO7/CE1   |              |

## Notes:
USB serial converter pinout
```
Black wire GND
White wire RXD
Green wire TXD
```
