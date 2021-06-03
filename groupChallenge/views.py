from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ChallengeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeListViewForUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChallengeListSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.filter(user=user)
        if user.is_authenticated:
            return Challenge.objects.filter(owner__in=profile)
        raise PermissionDenied()


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
    serializer_class = ChallengeListSerializer


class FeedbackAddView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackAddSerializer

