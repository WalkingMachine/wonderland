#!/usr/bin/env python

import requests
import json
import math
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from tf.transformations import quaternion_from_euler
import rviz_tools_py as rviz_tools

class object_publisher:

    def __init__(self):
        rospy.init_node('publish_wonderland_to_rviz', anonymous=False, log_level=rospy.INFO, disable_signals=False)

        self.markers = rviz_tools.RvizMarkers('/map', 'visualization_marker_wonderland')
        self.lifetime = 5.0

        self.publish_existing_model = {
            'table': self.publish_table,
            'chair': self.publish_chair,
            'couch': self.publish_couch,
            'living table': self.publish_living_table,
            'bed': self.publish_bed,
            'fridge': self.publish_fridge,
            'desk': self.publish_desk,
            'counter': self.publish_counter,
            'person': self.publish_human,
            'cupboard': self.publish_cupboard,
            'tv': self.publish_tv,
            'door': self.publish_door
        }

    def publish_door(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.01,0.01,0.01)
        mesh_file1 = "package://wonderland/models/door.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_human(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.035,0.035,0.035)
        mesh_file1 = "package://wonderland/models/human.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_tv(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.0013,0.0013, 0.0013)
        mesh_file1 = "package://wonderland/models/tv.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_counter(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.0035,0.0035,0.0035)
        mesh_file1 = "package://wonderland/models/counter.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_desk(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.017,0.017,0.017)
        mesh_file1 = "package://wonderland/models/desk.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_fridge(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.001,0.001,0.001)
        mesh_file1 = "package://wonderland/models/fridge.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_bed(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.0008,0.0008,0.0008)
        mesh_file1 = "package://wonderland/models/bed.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_living_table(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.01,0.01,0.01)
        mesh_file1 = "package://wonderland/models/living table.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_chair(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.02,0.02,0.02)
        mesh_file1 = "package://wonderland/models/chair.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_table(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.25,0.25,0.25)
        mesh_file1 = "package://wonderland/models/table.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_couch(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.007,0.007,0.007)
        mesh_file1 = "package://wonderland/models/couch.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)

    def publish_cupboard(self, pose, color):
        # Publish STL mesh of box, colored green
        scale = Vector3(0.012,0.012,0.012)
        mesh_file1 = "package://wonderland/models/cupboard.stl"
        self.markers.publishMesh(pose, mesh_file1, color, scale, self.lifetime)



    def wonderland_get_entity(self, args=None):
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

    def wonderland_get_person(self, args=None):
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
    def cleanup_node(self):
        print "Shutting down node"
        self.markers.deleteAllMarkers()

    def visualize(self):

        # Initialize the ROS Node
        self.lifetime = 7.0

        while not rospy.is_shutdown():

            entities = self.wonderland_get_entity()

            for entity in entities:
                if str(entity.get('entityCategory')).lower() == 'rooms':
                    # Publish some text using a ROS Pose Msg
                    P = Pose(Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0.2), Quaternion(0, 0, 0, 1))
                    scale = Vector3(0.3,0.3,0.3)
                    self.markers.publishText(P, str(entity.get('entityClass')), 'white', scale, 3.0)  # pose, text, color, scale, lifetime

                    # Publish a sphere using a ROS Point
                    point = Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0)
                    scale = Vector3(0.2,0.2,0.2)  # diameter
                    color = 'orange'
                    self.markers.publishSphere(point, color, scale, 3.0)  # pose, color, scale, lifetime

                    #color = 'red'
                    quat = quaternion_from_euler(0, 0, math.radians(entity.get('entityWaypointYaw')))
                    P_arrow = Pose(Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0.0),
                                   Quaternion(quat[0], quat[1], quat[2], quat[3]))
                    scale_arrow = Vector3(0.5, 0.1, 0.1)  # diameter
                    self.markers.publishArrow(P_arrow, color, scale_arrow, 3.0)

                if str(entity.get('entityCategory')).lower() == 'furniture':
                    # Publish some text using a ROS Pose Msg
                    P = Pose(Point(entity.get('entityPosX'), entity.get('entityPosY'), 0.2), Quaternion(0, 0, 0, 1))
                    scale = Vector3(0.3,0.3,0.3)
                    self.markers.publishText(P, str(entity.get('entityClass')), 'white', scale, 3.0)  # pose, text, color, scale, lifetime

                    # Publish a sphere using a ROS Point
                    if entity.get('entityPosX') != None:
                        if entity.get('entityPosZ') == None:
                            posZ = 0
                        else:
                            posZ = entity.get('entityPosZ')

                        point = Point(entity.get('entityPosX'), entity.get('entityPosY'), posZ)
                        scale = Vector3(0.2,0.2,0.2)  # diameter
                        color = 'blue'
                        self.markers.publishSphere(point, color, scale, 3.0)  # pose, color, scale, lifetime
                        scale_arrow = Vector3(0.5, 0.1, 0.1)  # diameter

                        if entity.get('entityWaypointX') != None and entity.get('entityWaypointYaw') != None:
                            quat = quaternion_from_euler(0, 0, math.radians(entity.get('entityWaypointYaw')))
                            P_arrow = Pose(Point(entity.get('entityWaypointX'), entity.get('entityWaypointY'), 0.2), Quaternion(quat[0],quat[1],quat[2],quat[3]))
                            self.markers.publishArrow(P_arrow, color, scale_arrow, 3.0)

                    if str(entity.get('entityClass')).lower() in self.publish_existing_model and entity.get('entityPosYaw') != None:

                        quat = quaternion_from_euler(0,0,math.radians(entity.get('entityPosYaw')))
                        color = 'white'
                        if str(entity.get('entityColor')).lower():
                            color = str(entity.get('entityColor')).lower()
                            self.publish_existing_model[str(entity.get('entityClass')).lower()](Pose(point, Quaternion(quat[0],quat[1],quat[2],quat[3])), color)

            rospy.Rate(1).sleep()  # 1 Hz

if __name__ == "__main__":
    pub = object_publisher()
    pub.visualize()