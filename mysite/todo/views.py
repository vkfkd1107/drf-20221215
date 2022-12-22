from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from todo.models import Todo
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins


# generic 구현
class TodoListAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
