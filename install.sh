#!/bin/bash

# This script will install wonderland

# Install pip and python developpement header
sudo apt install python python-pip python-dev -y

# Install requirements
sudo pip install -r requirements.txt

# Prepare application
python manage.py flush --noinput
python manage.py makemigrations --noinput
python manage.py migrate --run-syncdb --noinput

echo "Install done"
