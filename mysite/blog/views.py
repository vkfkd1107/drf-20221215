from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets


# viewset 구현
class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
