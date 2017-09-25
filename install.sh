#!/bin/bash

# This script will install wonderland

# install pip3 and python3 developpement header
sudo apt-get install python3 python3-pip python3-dev

git clone  https://github.com/WalkingMachine/wonderland.git

cd wonderland

pip3 install -r requirements.txt

echo "Install done"
