from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from todo.models import Todo
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import TodoSerializer


# First: class APIView를 기반으로 구현하기
class TodoList(APIView):
    def get(self, request, format=None):
        qs = Todo.objects.all()
        serializer = TodoSerializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)


class TodoDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Todo, pk=pk)
    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        print(todo)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
