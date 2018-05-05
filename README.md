# wonderland [![Build Status](https://travis-ci.org/WalkingMachine/wonderland.svg?branch=master)](https://travis-ci.org/WalkingMachine/wonderland)
API for One World Model

# Description
This API will help [S.A.R.A](http://walkingmachine.ca) to list all object she can see in her environment.

# Table of contents

- [Requirements](#requirements)
  * [Base](#base)
  * [Requirements](#requirements-1)
- [Installation](#installation)
- [Uses](#uses)
  * [For Entities](#for-entities)
    + [Add an entity in the list](#add-an-entity-in-the-list)
    + [Get all entities](#get-all-entities)
    + [Get an entity specified by ID](#get-an-entity-specified-by-id)
    + [Get an entity specified by position in area, in descriptive way](#get-an-entity-specified-by-position-in-area-in-descriptive-way)
- [HELP](#help)
  * [PostMan](#postman)
- [LICENCE](#licence)

# Requirements
Thing you need to install
## Base
- [Python](https://www.python.org/) 3.5
- [Django](https://www.djangoproject.com/) 1.11.2
- [Django rest_framework](http://www.django-rest-framework.org/)
- [Pip](https://pypi.python.org/pypi/pip?) for python 3.5

## Requirements
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

# Installation
1. First you have to install every python requirement
```bash
pip install -r requirements.txt
```

2. Reset database
```bash
python manage.py flush
```

3. Create a new superuser
```bash
python manage.py createsuperuser
```

4. Generate a new API key

+ Go to the api administration page (usually [localhost:8000/admin/](http://localhost:8000/admin/rest_framework_api_key/apikey/))

+ Create a new api-key

+ Save this api-key for use in the application or for test.

> The api-key will be given by a message like this: `The API Key for tests is 0801911fea20713b7416e88164a357eac6de3f3a. Please note it since you will not be able to see it again.`

5. Migration
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb 
```

6. Run server
```bash
python manage.py runserver
```

# Load/dump existing data  

### Dump data from actual database  
> python manage.py dumpdata api > api/wonderland_db.json 

### Load data from JSON file
> python manage.py loaddata api/wonderland_db.json


# Uses

## For Entities

Save all entities in the arena. Like rooms, objects, containers...

### Add an entity in the list

**Method:** POST

> TODO

### Get all entities

**URL:** `/api/entity`

**Method:** `GET`

**Request content:** `Nothing`

**Response content if success:** A list of areas with the following form:

|       key       |          description          |
|:---------------:|:-----------------------------:|
|    `entityId`   |  The id of the area           |
|  `entityClass`  |  The yolo class of the entity |
|  `entityName`   |  The name of the area         |

### Get an entity specified by ID

**URL:** `/api/entity`

**Method:** `GET`

**Request content:**

|    key   |         description         |
|:--------:|:---------------------------:|
|`entityId`|  The id of the entity       |

**Response content if success:** The entity corresponding to the request, with the following form:

|       key           |                  description                 |
|:-------------------:|:--------------------------------------------:|
|    `entityId`       |  The id of the entity                        |
|    `entityClass`    |  The yolo class of the entity                |
|    `entityName`     |  The name of the entity                      |
|  `entityCategory`   |  The category of the entity                  |
|  `entityContainer`  |  The container id of the entity              |
|    `entityPosX`     |  Abscissa coordinate of the entity           |
|    `entityPosY`     |  Ordinate coordinate of the entity           |
|    `entityPosZ`     |  Altitude coordinate of the entity           |
|   `entityPosYaw`    |  Yaw coordinate of the entity                |
|  `entityPosPitch`   |  Pitch coordinate of the entity              |
|   `entityPosRoll`   |  Roll coordinate of the entity               |
|  `entityWaypointX`  |  Abscissa of the waypoint of the entity      |
|  `entityWaypointY`  |  Ordinate of the waypoint of the entity      |
| `entityWaypointYaw` |  Yaw of the waypoint of the entity           |
|  `depth_waypoint`   |  Depth of kinship of the waypoint coordinate |
|  `depth_position`   |  Depth of kinship of the entity coordinate   |

### Get an entity specified by position in the arena, in a verbal way

**URL:** `/api/entity`

**Method:** `GET`

**Request content:** One or more of those parameters:

|        key       |            description            | optional |           Note           |
|:----------------:|:---------------------------------:|:--------:|:------------------------:|
|   `entityClass`  |  The yolo class of the entity     | &#10003; |                          |
| `entityCategory` |  The category of the object       | &#10003; |                          |
| `entityContainer`|  The yolo class of the container  | &#10003; | Can be an array of names |

**Response content if success:** A list of entities corresponding to the filters, with the following form:

|       key           |                  description                 |
|:-------------------:|:--------------------------------------------:|
|    `entityId`       |  The id of the entity                        |
|    `entityClass`    |  The yolo class of the entity                |
|    `entityName`     |  The name of the entity                      |
|  `entityCategory`   |  The category of the entity                  |
|  `entityContainer`  |  The container id of the entity              |
|    `entityPosX`     |  Abscissa coordinate of the entity           |
|    `entityPosY`     |  Ordinate coordinate of the entity           |
|    `entityPosZ`     |  Altitude coordinate of the entity           |
|   `entityPosYaw`    |  Yaw coordinate of the entity                |
|  `entityPosPitch`   |  Pitch coordinate of the entity              |
|   `entityPosRoll`   |  Roll coordinate of the entity               |
|  `entityWaypointX`  |  Abscissa of the waypoint of the entity      |
|  `entityWaypointY`  |  Ordinate of the waypoint of the entity      |
| `entityWaypointYaw` |  Yaw of the waypoint of the entity           |
|  `depth_waypoint`   |  Depth of kinship of the waypoint coordinate |
|  `depth_position`   |  Depth of kinship of the entity coordinate   |


# HELP
## PostMan
*Recommendation*
1. Installation see [here](https://www.getpostman.com/)

2. From Postman import `Walking Machine.postman_collection` located [here](../master/Walking%20Machine.postman_collection.json)

# LICENCE
Apache License 2.0
