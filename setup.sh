#!/bin/bash

# set the script to exit on any failure
set -e
mkdir -p logs/
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo apt-get install chromium-browser -y
sudo pip install requests
sudo pip install selenium==3.11
sudo apt-get install firefox -y
sudo apt-get install python-pip python-dev libmysqlclient-dev -y
sudo pip install mysqlclient

sudo chmod +x exploit*.sh
