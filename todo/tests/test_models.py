from django.test import TestCase

from todo.models import Tag


class ModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")

        self.assertEqual(str(tag), tag.name)
