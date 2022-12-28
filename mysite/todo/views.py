from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from todo.models import Todo
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


# modelviewset
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(ip=ip)
