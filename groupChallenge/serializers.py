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
        self.fields['owner'] = serializers.ReadOnlyField(source='owner.id')
        return super(ChallengeAddSerializer, self).to_representation(instance)


class ChallengeDetailSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    owner = UserSerializer(read_only=True, source='owner.user_name')
    users = UserSerializer(many=True, read_only=True)
=======
    owner = serializers.ReadOnlyField(source='owner.id')
    users = ProfileSerializer(many=True, read_only=True)
>>>>>>> challenge-api

    class Meta:
        model = Challenge
        fields = '__all__'


class FeedbackAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['owner'] = serializers.ReadOnlyField(source='owner.id')
        return super(FeedbackAddSerializer, self).to_representation(instance)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

