# wonderland
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
```
pip install -r requirements.txt
```

2. Migration
```
python manage.py makemigrations
python manage.py migrate
```

3. Run server
```
python manage.py runserver
```

## Usage

### PostMan
*Recommendation*

Import `Walking Machine.postman_collection`

### CURL
*TODO*
### Wget
*TODO*

## LICENCE
Apache License 2.0
