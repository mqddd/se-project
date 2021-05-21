from .serializers import *
from rest_framework import viewsets


class ChallengeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer


class ChallengeAddView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeAddSerializer


class ChallengeUpdateView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeAddSerializer


class ChallengeDeleteView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()


# test views
class UserDetailView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
