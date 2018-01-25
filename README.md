# wonderland [![Build Status](https://travis-ci.org/WalkingMachine/wonderland.svg?branch=devel)](https://travis-ci.org/WalkingMachine/wonderland)
API for One World Model

## Description
This API will help [S.A.R.A](http://walkingmachine.ca) to list all object she can see in her environment.

## Requirements
Thing you need to install
### Base
- [Python](https://www.python.org/) 3.5
- [Django](https://www.djangoproject.com/) 1.11.2
- [Django rest_framework](http://www.django-rest-framework.org/)
- [Pip](https://pypi.python.org/pypi/pip?) for python 3.5

### Requirements
- appdirs==1.4.3
- Django==1.11.2
- django-cors-headers==2.1.0
- djangorestframework==3.6.3
- drfapikey==0.0.3
- netifaces==0.10.5
- Markdown==2.6.8
- packaging==16.8
- pyparsing==2.2.0
- requests==2.13.0
- six==1.10.0

## Installation
1. First you have to install every python requirement
```bash
pip install -r requirements.txt
```

2. Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run server
```bash
python manage.py runserver
```

## Usage

### PostMan
*Recommendation*
1. Installation see [here](https://www.getpostman.com/)

2. From Postman import `Walking Machine.postman_collection` located [here](../master/Walking%20Machine.postman_collection.json)

### CURL
*TODO*

## TODO
- [ ] Make an Action list
- [ ] Make an API list
- [ ] Edit Model
- [ ] Add test File

## LICENCE
Apache License 2.0
