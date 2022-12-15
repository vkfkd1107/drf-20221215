from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # dispatch
    def dispatch(self, request, *args, **kwargs):
        print("request.body: ", request.body)
        print("request.POST: ", request.POST)
        return super().dispatch(request, *args, **kwargs)
