from django.views import generic
from django.shortcuts import render

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
