#!/usr/bin/env python

# Copyright (c) 2015, Carnegie Mellon University
# All rights reserved.
# Authors: David Butterworth <dbworth@cmu.edu>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# - Neither the name of Carnegie Mellon University nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""
This is a demo of Rviz Tools for python which tests all of the
available functions by publishing lots of Markers in Rviz.
"""

# Python includes
import numpy
import random
import requests
import sys
import json
import xml.etree.ElementTree as ET
import os
# ROS includes
import roslib
import math
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from tf import transformations  # rotation_matrix(), concatenate_matrices()
from tf.transformations import quaternion_from_euler
import rviz_tools_py as rviz_tools

# Initialize the ROS Node
rospy.init_node('test', anonymous=False, log_level=rospy.INFO, disable_signals=False)
lifetime = 7.0

def publish_door(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.01,0.01,0.01)
    mesh_file1 = "package://wonderland/models/door.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_human(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.035,0.035,0.035)
    mesh_file1 = "package://wonderland/models/human.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_tv(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.0013,0.0013, 0.0013)
    mesh_file1 = "package://wonderland/models/tv.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_counter(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.0035,0.0035,0.0035)
    mesh_file1 = "package://wonderland/models/counter.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_desk(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.017,0.017,0.017)
    mesh_file1 = "package://wonderland/models/desk.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_fridge(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.001,0.001,0.001)
    mesh_file1 = "package://wonderland/models/fridge.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_bed(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.0008,0.0008,0.0008)
    mesh_file1 = "package://wonderland/models/bed.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_living_table(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.01,0.01,0.01)
    mesh_file1 = "package://wonderland/models/living table.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_chair(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.02,0.02,0.02)
    mesh_file1 = "package://wonderland/models/chair.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_table(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.25,0.25,0.25)
    mesh_file1 = "package://wonderland/models/table.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_couch(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.007,0.007,0.007)
    mesh_file1 = "package://wonderland/models/couch.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

def publish_cupboard(pose, color):
    # Publish STL mesh of box, colored green
    scale = Vector3(0.012,0.012,0.012)
    mesh_file1 = "package://wonderland/models/cupboard.stl"
    markers.publishMesh(pose, mesh_file1, color, scale, lifetime) # pose, mesh_file_name, color, mesh_scale, lifetime

publish_existing_model = {
    'table': publish_table,
    'chair': publish_chair,
    'couch': publish_couch,
    'living table': publish_living_table,
    'bed': publish_bed,
    'fridge': publish_fridge,
    'desk': publish_desk,
    'counter': publish_counter,
    'person': publish_human,
    'cupboard': publish_cupboard,
    'tv': publish_tv,
    'door': publish_door
}

def wonderland_get_entity(args=None):
    url = "http://localhost:8000/api/entity/"

    headers = {
        'api-key': "43d5d4a6b88c4c2ea303188fcbc3385f79d1e961",
        'cache-control': "no-cache",
        'postman-token': "c0ef09c6-ad86-b7f4-52be-fe3c0f6d1238"
    }
    response = None

    if args != None:
        response = requests.get(url, headers=headers, params=args)
    else:
        response = requests.get(url, headers)

    parsedJson = json.loads(response.text)

    return parsedJson

def wonderland_get_person(args=None):
    url = "http://localhost:8000/api/people/"

    headers = {
        'api-key': "43d5d4a6b88c4c2ea303188fcbc3385f79d1e961",
        'cache-control': "no-cache",
        'postman-token': "c0ef09c6-ad86-b7f4-52be-fe3c0f6d1238"
    }
    response = None

    if args != None:
        response = requests.get(url, headers=headers, params=args)
    else:
        response = requests.get(url, headers)

    parsedJson = json.loads(response.text)

    return parsedJson


# Define exit handler
def cleanup_node():
    print "Shutting down node"
    markers.deleteAllMarkers()


rospy.on_shutdown(cleanup_node)

markers = rviz_tools.RvizMarkers('/map', 'visualization_marker_wonderland')

while not rospy.is_shutdown():

    entities = wonderland_get_entity()

    for entity in entities:
        if str(entity.get('entityCategory')).lower() == 'rooms':
            # Publish some text using a ROS Pose Msg
            P = Pose(Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0.2), Quaternion(0, 0, 0, 1))
            scale = Vector3(0.3,0.3,0.3)
            markers.publishText(P, str(entity.get('entityClass')), 'white', scale, 3.0)  # pose, text, color, scale, lifetime

            # Publish a sphere using a ROS Point
            point = Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0)
            scale = Vector3(0.2,0.2,0.2)  # diameter
            color = 'orange'
            markers.publishSphere(point, color, scale, 3.0)  # pose, color, scale, lifetime

        if str(entity.get('entityCategory')).lower() == 'furniture':
            # Publish some text using a ROS Pose Msg
            P = Pose(Point(entity.get('entityPosX'), entity.get('entityPosY'), 0.2), Quaternion(0, 0, 0, 1))
            scale = Vector3(0.3,0.3,0.3)
            markers.publishText(P, str(entity.get('entityClass')), 'white', scale, 3.0)  # pose, text, color, scale, lifetime

            # Publish a sphere using a ROS Point
            if entity.get('entityPosX') != None:
                if entity.get('entityPosZ') == None:
                    posZ = 0
                else:
                    posZ = entity.get('entityPosZ')

                point = Point(entity.get('entityPosX'), entity.get('entityPosY'), posZ)
                scale = Vector3(0.2,0.2,0.2)  # diameter
                color = 'blue'
                markers.publishSphere(point, color, scale, 3.0)  # pose, color, scale, lifetime

            if str(entity.get('entityClass')).lower() in publish_existing_model and entity.get('entityPosYaw') != None:
                #print(str(entity.get('entityClass')).lower())
                quat = quaternion_from_euler(0,0,math.radians(entity.get('entityPosYaw')))
                color = 'white'
                if str(entity.get('entityColor')).lower():
                    color = str(entity.get('entityColor')).lower()
                publish_existing_model[str(entity.get('entityClass')).lower()](Pose(point, Quaternion(quat[0],quat[1],quat[2],quat[3])), color)



    # Publish a sphere using a ROS Point
    #point = Point(-4.4, -2.5, 0)
    #scale = Vector3(0.7, 0.7, 0.7)  # diameter
    #color = 'orange'
    #markers.publishSphere(point, color, scale, 5.0)  # pose, color, scale, lifetime




    rospy.Rate(1).sleep()  # 1 Hz