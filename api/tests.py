from django.test import TestCase
from api.models import Entity, Human, Object
# Create your tests here.


class EntityTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.entity = Entity.objects.create(
            name="entity_test",
            time=None
        )

        cls.entity_human = Entity.objects.create(
            name="entity_human",
            time=None
        )
        cls.human = Human.objects.create(
            entity=cls.entity_human
        )

        cls.entity_object = Entity.objects.create(
            name="entity_object",
            time=None
        )

        cls.object = Object.objects.create(
            entity=cls.entity_object
        )

    def testEntityCreation(self):
        entity = self.entity
        self.assertEqual(entity.name, "entity_test")

    def testHumanCreation(self):
        human = self.human
        self.assertEqual(human.entity.name, "entity_human")

    def testObjectCreation(self):
        object = self.object
        self.assertEqual(object.entity.name, "entity_object")
