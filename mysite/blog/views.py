from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics, mixins, viewsets
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


# template html renderer 구현
class PostList(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response({
            'posts': self.get_queryset()
        }, template_name='post_list.html')


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'post.html'

    def get(self, request, *args, **kwargs):
        return Response({
            'post': self.get_object()
        })


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def static_view(request):
    data = "<html><body><h1>Hello, Here is Blog App</h1></body></html>"
    return Response(data)


@api_view(['GET'])
def format_view_blog(request, format=None):
    return Response([])
