from rest_framework import serializers
from todo.models import ToDoList
from todo.models import Task

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id','name','icon']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','list','title']