#!/bin/sh
#launcher.sh # navigate to home directory, then to this directory, then execute python script, then back home
locale
cd /
cd /home/admin/pi/scripts/
sudo python3 ./fan_ctrl.py &
cd /
