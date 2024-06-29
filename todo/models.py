from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Task(models.Model):
    list = models.ForeignKey(ToDoList, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
