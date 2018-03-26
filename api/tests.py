from django.test import TestCase
from api.models import Entity
# Create your tests here.


class EntityTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.entity = Entity.objects.create(
            name="entity_test",
            type="bitch",
            x_position=10.2,
            y_position=1.12
            )
