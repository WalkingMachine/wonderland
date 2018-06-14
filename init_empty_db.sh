#!/usr/bin/env bash

echo "This will errase the entire Wonderland database."
echo "Are you sure you want to do that ? (yes/no)"
read -r
if [[ $REPLY =~ 'yes' ]]
then
    echo "Will save DB."
    mkdir -p backup
    touch "backup/backup-$(date +'%m%d%y-%R').json"
    ./manage.py dumpdata > "backup/backup-$(date +'%m%d%y-%R').json"

    # Remove previous DB
    sudo rm ./db.sqlite3

    # Initialise an empty DB
    python manage.py makemigrations
    python manage.py migrate --run-syncdb

    # Create a superuser
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell
    
    # Start server
    echo "START DJANGO SERVER" 
    python manage.py runserver

fi

