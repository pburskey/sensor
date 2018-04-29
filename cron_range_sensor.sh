#!/bin/sh
HOME=/home/pi
LOGNAME=pi
PATH=/usr/bin:/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/home/pi


git config --global user.name pburskey
git config --local user.email pburskey@msn.com

git pull
python /home/pi/projects/sensor/monitor_and_report.py
