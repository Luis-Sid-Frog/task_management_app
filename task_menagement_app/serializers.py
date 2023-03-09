from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

from .models import Task
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    # users = UserSerializer(read_only=True, many=False)

    def create(self, validated_data):
        task = Task.objects.create(
            title = validated_data['title'],
            description = validated_data['description'],
            status = validated_data['status'],
            user = self.get_user_from_db(validated_data['user_request_id'])
        )
        task.save()
        return task

    def get_user_from_db(self, user_id):
        if len(User.objects.filter(id=user_id).all()) == 0:
            raise Exception('Użytkownik nie isniteje ')
        else:
            return User.objects.filter(id=user_id).all()[0]

    class Meta:
        model = Task
        fields = ('id','title','description','status','user_request_id')


class TaskListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id','title','description','status','user')
