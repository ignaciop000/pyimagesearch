#!/bin/bash

source /home/pi/.profile
workon cv
cd /home/pi/pi-reboot
python pi_reboot_alarm.py
