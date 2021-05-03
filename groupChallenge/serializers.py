from rest_framework import serializers
from .models import *


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'like_number', 'days', 'start_date', 'end_date', 'progress_type', 'icon',
                  'private_public_type']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'password']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']
