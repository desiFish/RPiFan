#!/bin/sh
# fanService.sh
# navigate to home directory, then to this directory, then execute python script, then back home
cd /
cd /home/admin/projects/RPiFan/
sudo python3 ./fan_control.py
cd /
