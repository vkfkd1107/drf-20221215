from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    useremail = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Todo
        fields = '__all__'
