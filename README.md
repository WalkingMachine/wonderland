# wonderland [![Build Status](https://travis-ci.org/WalkingMachine/wonderland.svg?branch=master)](https://travis-ci.org/WalkingMachine/wonderland)
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
- django-unixtimestampfield==0.3.9

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

## Features

### For Entities

> TODO

### Spaces

Save all rooms and spaces in the arena.

#### POST

Add an object in the list.

**Body:**

|    key    |         description         | optional |
|:---------:|:---------------------------:|:--------:|
|  `name`   |  The name of the space      |          |
| `x_left`  |  The left delimiter         |          |
| `x_right` |  The right delimiter        |          |
|  `y_top`  |  The top delimiter          |          |
| `y_bottom`|  The bottom delimiter       |          |

**Response:**

|   key    |         description         |
|:--------:|:---------------------------:|
|`space_id`|  The id of the space        |
|  `name`  |  The name of the space      |
| `x_left` |  The left delimiter         |
|`x_right` |  The right delimiter        |
| `y_top`  |  The top delimiter          |
|`y_bottom`|  The bottom delimiter       |

#### GET

Get the room designed by the entered id or name. The priority is on the id.

> TODO: Add search by geolocation

**Body:**

|    key   |         description         | optional |
|:--------:|:---------------------------:|:--------:|
|`space_id`|  The name of the space      | &#10003; |
|  `name`  |  The name of the space      | &#10003; |

## Usage
### PostMan
*Recommendation*
1. Installation see [here](https://www.getpostman.com/)

2. From Postman import `Walking Machine.postman_collection` located [here](../master/Walking%20Machine.postman_collection.json)

## LICENCE
Apache License 2.0
