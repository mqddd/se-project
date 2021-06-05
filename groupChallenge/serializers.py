from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = User
        fields = ['id', 'user_name', 'email']


class ChallengeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'like_number', 'start_date', 'end_date', 'categories'
                  , 'icon', 'private_public_type']


class ChallengeAddSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['owner'] = serializers.ReadOnlyField(source='owner.id')
        return super(ChallengeAddSerializer, self).to_representation(instance)


class ChallengeDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    users = serializers.StringRelatedField(many=True, read_only=True)

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


class JoinPublicChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserChallengeProgress
        fields = ['user', 'challenge']

    def to_representation(self, instance):
        self.fields['user'] = serializers.ReadOnlyField(source='user.id')
        self.fields['challenge'] = serializers.ReadOnlyField(source='challenge.id')
        return super(JoinPublicChallengeSerializer, self).to_representation(instance)


class JoinPrivateChallengeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True, allow_null=False)
    challenge_id = serializers.IntegerField(required=True, allow_null=False)
    password = serializers.CharField(required=True, allow_null=False)

