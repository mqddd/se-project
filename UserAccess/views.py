from django.shortcuts import render
from groupChallenge.models import User
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer


class UserDetial (RetrieveUpdateAPIView):
    queryset = User.objects.all()
    Serializer_class = UserSerializer
