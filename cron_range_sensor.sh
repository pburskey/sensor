#!/bin/sh
HOME=/home/pi
LOGNAME=pi
PATH=/usr/bin:/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/home/pi

#git pull
python /home/pi/projects/sensor/monitor_and_report.py
