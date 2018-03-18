#!/bin/bash

# set the script to exit on any failure
set -e

sudo apt-get update -y
sudo apt-get install python-pip -y
sudo apt-get install chromium-browser -y
sudo pip install requests
sudo pip install selenium
sudo apt-get install firefox -y
