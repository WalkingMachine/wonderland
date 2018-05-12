from __future__ import print_function

import json

from django.test import TestCase

from models import Entity


class EntityTest(TestCase):
    def setUp(self):
        e1 = Entity.objects.create(entityClass="dining room", entityContainer=None,
                                   entityIsWaypoint=True, entityWaypointX=0, entityWaypointY=5)         # 1
        e2 = Entity.objects.create(entityClass="bedroom", entityContainer=None, entityIsWaypoint=True,
                                   entityWaypointX=12, entityWaypointY=15, entityWaypointYaw=2.3)       # 2
        e3 = Entity.objects.create(entityClass="table", entityContainer=e1)                             # 3
        Entity.objects.create(entityClass="chair", entityContainer=e1,)                                 # 4
        e5 = Entity.objects.create(entityClass="sideboard", entityContainer=e1)                         # 5
        Entity.objects.create(entityClass="cut", entityContainer=e3,)                                   # 6
        Entity.objects.create(entityClass="apple", entityContainer=e3, entityCategory="fruit")          # 7
        e8 = Entity.objects.create(entityClass="tray", entityContainer=e3,)                             # 8
        Entity.objects.create(entityClass="apple", entityContainer=e8, entityCategory="fruit")          # 9
        Entity.objects.create(entityClass="glass", entityContainer=e5)                                  # 10
        Entity.objects.create(entityClass="glass", entityContainer=e3)                                  # 11
        Entity.objects.create(entityClass="bed", entityContainer=e2)                                    # 12
        e13 = Entity.objects.create(entityClass="night table", entityContainer=e2)                      # 13
        Entity.objects.create(entityClass="clock", entityContainer=e13)                                 # 14
        Entity.objects.create(entityClass="light", entityContainer=e13)                                 # 15
        e16 = Entity.objects.create(entityClass="table", entityContainer=e2)                            # 16
        Entity.objects.create(entityClass="cut", entityContainer=e16)                                   # 17
        Entity.objects.create(entityClass="pen", entityContainer=e16)                                   # 18
        Entity.objects.create(entityClass="desk", entityContainer=e2,
                              entityIsWaypoint=True, entityWaypointX=-10, entityWaypointY=-15)          # 19
        Entity.objects.create(entityClass="chair", entityContainer=e2)                                  # 20

    def test_get_by_id_view(self):
        response = self.client.get('/api/entity/', {'entityId': 1})
        entity = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(entity['entityId'], 1)
        self.assertEqual(entity['entityClass'], 'dining room')
        self.assertEqual(entity['entityWaypointX'], 0)
        self.assertEqual(entity['entityWaypointY'], 5)
        self.assertEqual(entity['depth_waypoint'], 0)
        self.assertEqual(entity['depth_position'], None)

    def test_get_by_id_location_parent(self):
        response = self.client.get('/api/entity/', {'entityId': 18})
        entity = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(entity['entityId'], 18)
        self.assertEqual(entity['entityClass'], 'pen')
        self.assertEqual(entity['entityWaypointX'], 12)
        self.assertEqual(entity['entityWaypointY'], 15)
        self.assertEqual(entity['entityWaypointYaw'], 2.3)
        self.assertEqual(entity['depth_waypoint'], 2)
        self.assertEqual(entity['depth_position'], None)

    def test_get_multiple_object_in_same_room(self):
        response = self.client.get('/api/entity/', {'entityClass': 'apple'})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 2)
        self.assertEqual(entity[0]['entityId'], 7)
        self.assertEqual(entity[1]['entityId'], 9)

    def test_get_multiple_object_in_different_room(self):
        response = self.client.get('/api/entity/', {'entityClass': 'cut'})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 2)
        self.assertEqual(entity[0]['entityId'], 6)
        self.assertEqual(entity[1]['entityId'], 17)

    def test_get_single_object_by_name_in_container(self):
        response = self.client.get('/api/entity/', {'entityClass': 'apple', 'entityContainer': 'tray'})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 1)
        self.assertEqual(entity[0]['entityId'], 9)

    def test_get_single_object_by_name_in_container_room(self):
        response = self.client.get('/api/entity/', {'entityClass': 'chair', 'entityContainer': 'bedroom'})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 1)
        self.assertEqual(entity[0]['entityId'], 20)

    def test_get_multiple_objects_in_multiple_container(self):
        response = self.client.get('/api/entity/', {'entityContainer': ['bedroom', 'table']})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 4)
        self.assertEqual(entity[0]['entityId'], 14)
        self.assertEqual(entity[1]['entityId'], 15)
        self.assertEqual(entity[2]['entityId'], 17)
        self.assertEqual(entity[3]['entityId'], 18)

    def test_get_objects_by_category(self):
        response = self.client.get('/api/entity/', {'entityCategory': 'fruit'})
        entity = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(entity), 2)
        self.assertEqual(entity[0]['entityId'], 7)
        self.assertEqual(entity[1]['entityId'], 9)

    def test_post_object_with_waypoint(self):
        response = self.client.post('/api/entity/', {'entityClass': 'living room',
                                                     'entityWaypointX': -10, 'entityWaypointY': -15})
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/entity/', {'entityId': 21})
        self.assertEqual(response.status_code, 200)

        entity = json.loads(response.content)
        self.assertEqual(entity['entityId'], 21)
        self.assertEqual(entity['entityWaypointX'], -10)
        self.assertEqual(entity['entityWaypointY'], -15)
        self.assertEqual(entity['depth_waypoint'], 0)
        self.assertEqual(entity['depth_position'], None)

    def test_post_object_in_room_with_waypoint(self):
        response = self.client.post('/api/entity/', {'entityClass': 'banana',
                                                     'entityContainer': 19,
                                                     'entityPosX': 2, 'entityPosY': 22, 'entityPosZ': 1.5})

        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/entity/', {'entityId': 21})
        self.assertEqual(response.status_code, 200)

        entity = json.loads(response.content)
        self.assertEqual(entity['entityContainer'], 19)
        self.assertEqual(entity['entityWaypointX'], -10)
        self.assertEqual(entity['entityWaypointY'], -15)
        self.assertEqual(entity['entityPosX'], 2)
        self.assertEqual(entity['entityPosY'], 22)
        self.assertEqual(entity['entityPosYaw'], None)
        self.assertEqual(entity['depth_waypoint'], 1)
        self.assertEqual(entity['depth_position'], 0)

        # TODO: Add tests for People requests...
