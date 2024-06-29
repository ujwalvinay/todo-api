from django.http import JsonResponse
from .models import ToDoList
from .serializers import TodoSerializer

from .models import Task
from .serializers import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def todo_list(request, format=None):

    if request.method == 'GET':
        todo = ToDoList.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET','DELETE','PUT'])
def todo_detail(request, id, format=None):

        try:
           todo =  ToDoList.objects.get(pk=id)
        except ToDoList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = TodoSerializer(todo, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        


@api_view(['GET','POST'])
def task_list(request, format=None):

    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
  

@api_view(['GET', 'POST', 'DELETE'])
def tasks_detail(request, id, format=None):
    try:
        tasks = Task.objects.filter(list=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(list_id=id)  # Assign list_id to the new task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
def single_task_detail(request, list_id, task_id, format=None):
    try:
        task = Task.objects.get(pk=task_id, list_id=list_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = TaskSerializer(task, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)