from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from todo.models import Todo
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics
from rest_framework import mixins
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


# tempate renderer 구현
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request, *args, **kwargs):
        return Response({
            'posts': self.get_queryset()
        })


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo.html'

    def get(self, request, *args, **kwargs):
        return Response({
            'post': self.get_object()
        })


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def static_html_renderer(request):
    data = "<html><body><h1>Hello, Here is Todo App</h1></body></html>"
    return Response(data)


@api_view(['GET'])
def format_renderer(request, format=None):
    return Response([])
