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
  * [For area](#for-area)
    + [Add an area in the list](#add-an-area-in-the-list)
    + [Get all areas](#get-all-areas)
    + [Get specified area](#get-specified-area)
    + [Get an area corresponding to a position in the arena](#get-an-area-corresponding-to-a-position-in-the-arena)
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

2. Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run server
```bash
python manage.py runserver
```

# Uses

## For Entities

> TODO

## For area

Save all areas in the arena.

### Add an area in the list

**Method:** POST

**Request content:**

|    key    |         description         | optional |
|:---------:|:---------------------------:|:--------:|
|  `name`   |  The name of the space      |          |
| `x_left`  |  The left delimiter         |          |
| `x_right` |  The right delimiter        |          |
|  `y_top`  |  The top delimiter          |          |
| `y_bottom`|  The bottom delimiter       |          |

**Response content if success:** A list of areas with the following form:

|   key    |         description         |
|:--------:|:---------------------------:|
|`space_id`|  The id of the space        |
|  `name`  |  The name of the space      |
| `x_left` |  The left delimiter         |
|`x_right` |  The right delimiter        |
| `y_top`  |  The top delimiter          |
|`y_bottom`|  The bottom delimiter       |

**Response if data missing:** A list of missing datas with code `400`.

### Get all areas

**Method:** GET

**Request content:** Nothing

**Response content if success:** A list of areas with the following form:

|   key    |         description         |
|:--------:|:---------------------------:|
|`space_id`|  The id of the area         |
|  `name`  |  The name of the area       |
| `x_left` |  The left delimiter         |
|`x_right` |  The right delimiter        |
| `y_top`  |  The top delimiter          |
|`y_bottom`|  The bottom delimiter       |

### Get specified area

**Method:** GET

**Request content:** One of the following key (id is prefered as name if there is both):

|    key   |         description         | optional |
|:--------:|:---------------------------:|:--------:|
|`space_id`|  The id of the area         | &#10003; |
|  `name`  |  The name of the area       | &#10003; |

**Response content if success:** A list of areas corresponding to the request, with the following form:

|   key    |         description         |
|:--------:|:---------------------------:|
|`space_id`|  The id of the space        |
|  `name`  |  The name of the space      |
| `x_left` |  The left delimiter         |
|`x_right` |  The right delimiter        |
| `y_top`  |  The top delimiter          |
|`y_bottom`|  The bottom delimiter       |

### Get an area corresponding to a position in the arena

**Method:** GET

**Request content:** The position in the arena of an object, with the following form:

|     key    |         description         | optional |
|:----------:|:---------------------------:|:--------:|
|`x_position`|  x position of the point    |          |
|`y_position`|  y position of the point    |          |

**Response content if success:** A list of areas corresponding to the request, with the following form:

|   key    |         description         |
|:--------:|:---------------------------:|
|`space_id`|  The id of the space        |
|  `name`  |  The name of the space      |
| `x_left` |  The left delimiter         |
|`x_right` |  The right delimiter        |
| `y_top`  |  The top delimiter          |
|`y_bottom`|  The bottom delimiter       |

# HELP
## PostMan
*Recommendation*
1. Installation see [here](https://www.getpostman.com/)

2. From Postman import `Walking Machine.postman_collection` located [here](../master/Walking%20Machine.postman_collection.json)

# LICENCE
Apache License 2.0
