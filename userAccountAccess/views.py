from .models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer


class UserDetailView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
