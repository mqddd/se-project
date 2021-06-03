from django.contrib.auth import get_user_model
from rest_framework import serializers
from groupChallenge.models import Profile

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'},
                                             write_only=True, label='Confirm password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError(
                {'email': 'Email addresses must be unique.'})
        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'The two passwords differ.'})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        profile = Profile(user=user)
        profile.save()
        return user
