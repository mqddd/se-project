from rest_framework import serializers
from .models import *


class ChallengeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'like_number', 'start_date', 'end_date', 'category'
                  , 'icon', 'private_public_type']


class ChallengeAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_name', 'avatar']


class ChallengeDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user_name')
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'days', 'like_number', 'start_date', 'end_date', 'progress_type'
                  , 'icon', 'private_public_type', 'category', 'owner', 'users']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'description']
