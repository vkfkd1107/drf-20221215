from wsgiref.validate import validator
from rest_framework import serializers
from todo.models import Todo
from rest_framework.validators import ValidationError, UniqueValidator, UniqueTogetherValidator


class TodoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    useremail = serializers.ReadOnlyField(source='user.email')
    title = serializers.CharField(max_length=10)

    def validate(self, data):
        if 'post' not in data['title']:
            raise ValidationError('post가 제목에 포함되야합니다')
        return data

    class Meta:
        model = Todo
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Todo.objects.all(),
                fields=['title'],
                message='똑같은 제목이 있습니다. 다른 제목으로 바꿔주세요'
            )
        ]
