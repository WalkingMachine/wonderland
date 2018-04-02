from __future__ import print_function
from django.test import TestCase
from api.models import Area
import json
# Create your tests here.


class AreaTest(TestCase):
    def setUp(self):
        Area.objects.create(name="kitchen", x_left=0, x_right=10, y_top=10, y_bottom=0)
        Area.objects.create(name="bathroom", x_left=10, x_right=20, y_top=10, y_bottom=0)
        Area.objects.create(name="living", x_left=-10, x_right=0, y_top=10, y_bottom=0)

    def test_get_by_id_view(self):
        response = self.client.get('/api/area/', {'id': 1})
        area = json.loads(response.content)[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(area['name'], 'kitchen')
        self.assertEqual(area['x_left'], 0)
        self.assertEqual(area['x_right'], 10)
        self.assertEqual(area['y_top'], 10)
        self.assertEqual(area['y_bottom'], 0)

    def test_get_by_name_view(self):
        response = self.client.get('/api/area/', {'name': 'kitchen'})
        area = json.loads(response.content)[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(area['x_left'], 0)
        self.assertEqual(area['x_right'], 10)
        self.assertEqual(area['y_top'], 10)
        self.assertEqual(area['y_bottom'], 0)

    def test_get_by_location_view(self):
        response = self.client.get('/api/area/', {'x_position': -5, 'y_position': 5})
        area = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(area['name'], 'living')
