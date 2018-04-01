from __future__ import print_function
from django.test import TestCase
from api.models import Entity
# Create your tests here.


class EntityTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("ok")
