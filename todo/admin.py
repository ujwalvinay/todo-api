from django.contrib import admin
from .models import ToDoList
from .models import Task

admin.site.register(ToDoList)
admin.site.register(Task)