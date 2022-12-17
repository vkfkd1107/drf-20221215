from rest_framework import serializers
from blog.models import Post
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'context',
            'created_at',
            'updated_at',
            'author',
        ]
