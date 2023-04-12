from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag

TASK_URL = reverse("todo:task-list")
TAG_URL = reverse("todo:tag-list")


class PrivateTaskTests(TestCase):
    def test_retrieve_tasks(self):
        Task.objects.create(
            content="test_content",
            deadline=datetime(2023, 4, 30, 12, 00)
        )

        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "todo/task_list.html")


class PrivateTagTests(TestCase):
    def test_retrieve_tags(self):
        Tag.objects.create(
            name="test_tag"
        )

        response = self.client.get(TAG_URL)
        tags = Tag.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )
        self.assertTemplateUsed(response, "todo/tag_list.html")


class TaskChangeStatusViewTests(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            content="test_content",
            deadline=datetime(2023, 4, 30, 12, 00),
            is_completed=False
        )
        self.url = reverse("todo:change-status", args=[self.task.pk])

    def test_change_task_status(self):
        response = self.client.post(self.url)
        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.task.is_completed)

        response = self.client.post(self.url)
        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.task.is_completed)
