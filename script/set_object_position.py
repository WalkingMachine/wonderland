#!/usr/bin/env python
import string
import rospy
import requests


from geometry_msgs.msg import PointStamped, PoseWithCovarianceStamped
import tf
import json
import math

class set_object_position:

    def __init__(self):
        self.id = None
        self.mode_str = None
        self.mode = 0 # mode : 0=none, 1=position, 2=waypoint
        rospy.init_node('set_object_position', anonymous=True)

        self.sub = rospy.Subscriber("initialpose", PoseWithCovarianceStamped, self.callback_pose)

        self.headers = {
            'api-key': "43d5d4a6b88c4c2ea303188fcbc3385f79d1e961",
            'cache-control': "no-cache",
            'postman-token': "c0ef09c6-ad86-b7f4-52be-fe3c0f6d1238"
        }

        self.url = "http://localhost:8000/api/entity/"

    def callback_pose(self, data):
        if data.header.frame_id != "map":
            print "-----------------------------------"
            print "WATCHOUT, THE FRAME IS NOT ON /MAP"
            print "-----------------------------------"
        else:
            if self.id != None:
                if self.mode == 1:
                    self.wonderland_set_position(self.id,data.pose)
                elif self.mode == 2:
                    self.wonderland_set_waypoint(self.id, data.pose)
            else:
                print "-----------------------------------"
                print "        ENTITY_ID NOT SET"
                print "-----------------------------------"


    def pose_to_angle(self, pose):
        quaternion = (
            pose.pose.orientation.x,
            pose.pose.orientation.y,
            pose.pose.orientation.z,
            pose.pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        return math.degrees(euler[2])


    def wonderland_set_position(self, entityId, pose):

        body = {
            'entityId' : entityId,
            'entityPosX' : pose.pose.position.x,
            'entityPosY' : pose.pose.position.y,
            'entityPosYaw' : self.pose_to_angle(pose)
        }

        response = None

        if body != None:
            response = requests.patch(self.url, headers=self.headers, data=body)


    def wonderland_set_waypoint(self, entityId, pose):

        body = {
            'entityId' : entityId,
            'entityWaypointX' : pose.pose.position.x,
            'entityWaypointY' : pose.pose.position.y,
            'entityWaypointYaw' : self.pose_to_angle(pose)
        }

        response = None

        if body != None:
            response = requests.patch(self.url, headers=self.headers, data=body)


    def wonderland_list_entities(self):

        response = None
        response = requests.get(self.url, headers=self.headers)
        parsedJson = json.loads(response.text)
        for entity in parsedJson:
            str_id = "ID : " + str(entity.get('entityId'))
            str_category = "(" + str(entity.get('entityCategory')) + ")"
            str_class = "Class : " + str(entity.get('entityClass'))
            str_container = "Container : " + str(entity.get('entityContainer'))
            str_finale = str_id
            for i in range(0,8-len(str_id)):
                str_finale += " "
            str_finale += str_category
            for i in range(0,25-len(str_finale)):
                str_finale += " "
            str_finale += str_class
            for i in range(0, 25 - len(str_class)):
                str_finale += " "
            str_finale += str_container

            print str_finale

    def wonderland_get_class(self, entityId):

        try:
            if entityId != None:
                response = None
                arg = {'entityId' : entityId}
                response = requests.get(self.url, headers=self.headers, params=arg)
                parsedJson = json.loads(response.text)
                return "(" + str(parsedJson.get('entityClass')) + ")"
            return ""
        except:
            return "(not in db)"

    def getchar(self):
        # Returns a single character from standard input
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def menu(self):
        try:
            command = ""
            while True:
                print "|------------------------------------|"
                print "|  Press <Q> or <q> to exit          |"
                print "|------------------------------------|"
                print "|  Current entity : " + str(self.id) + str(self.wonderland_get_class(self.id))
                print "|  Current mode : " + str(self.mode_str)
                print "|------------------------------------|"
                print "|  prev <a>  <d> next                |"
                print "|  1. Set entity id                  |"
                print "|  2. Set entity position            |"
                print "|  3. Set entity waypoint            |"
                print "|  4. List entities                  |"
                print "|------------------------------------|\n"

                command = self.getchar()
                if command == "1":
                    id = raw_input("Entity:")
                    self.id = int(id)
                if command == "2":
                    print "Set entity position"
                    self.mode = 1
                    self.mode_str = "position"
                elif command == "3":
                    print "Set entity waypoint"
                    self.mode = 2
                    self.mode_str = "waypoint"
                elif command == "4":
                    print "List entities"
                    self.wonderland_list_entities()
                elif command == "a":
                    if self.id == None:
                        self.id = 1;
                    elif self.id > 1:
                        self.id -= 1
                elif command == "d":
                    if self.id == None:
                        self.id = 1;
                    elif self.id > 0:
                        self.id += 1
                elif command == 'q' or command == 'Q':
                    break
        except KeyboardInterrupt:
            print "Goodbye"



if __name__ == "__main__":
    pub = set_object_position()
    pub.menu()
