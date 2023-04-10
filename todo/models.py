from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
