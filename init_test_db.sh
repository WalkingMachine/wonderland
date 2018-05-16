#!/usr/bin/env bash

# Remove previous DB
rm ./db.sqlite3

# Initialise an empty DB
python manage.py makemigrations
python manage.py migrate --run-syncdb

# Start server
python manage.py runserver &

# Create a superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell

# Add test data in DB
cat generate_test_db.py | python manage.py shell
