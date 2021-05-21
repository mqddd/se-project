from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'user_name', 'email', 'avatar']


class ChallengeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'like_number', 'start_date', 'end_date', 'category'
                  , 'icon', 'private_public_type']


class ChallengeAddSerializer(serializers.ModelSerializer):
    users = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['owner'] = ProfileSerializer(read_only=True)
        return super(ChallengeAddSerializer, self).to_representation(instance)


class ChallengeDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.user.username')
    owner = serializers.ReadOnlyField(source='owner.id')
    users = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'days', 'like_number', 'start_date', 'end_date', 'progress_type'
                  , 'icon', 'private_public_type', 'category', 'owner', 'users']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'description']

