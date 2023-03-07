from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title','description','status')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = get_user_model()
        fields = ('username','password')