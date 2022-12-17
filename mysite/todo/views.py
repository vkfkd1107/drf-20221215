from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from todo.models import Todo
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view


# First: function view로 구현하기
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    else:
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
