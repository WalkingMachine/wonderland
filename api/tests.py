from django.test import TestCase
from api.models import Entity, Human, Object, ArTag
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

        cls.entity_artag = Entity.objects.create(
            name="entity_artag",
            time=None
        )

        cls.ar_tag = ArTag.objects.create(
            entity=cls.entity_artag
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

    def testArTagCreation(self):
        ar_tag = self.ar_tag
        self.assertEqual(ar_tag.entity.name, "entity_artag")
