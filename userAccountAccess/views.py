from .models import Profile
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
