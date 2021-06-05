from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class PublicChallengeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(private_public_type='PU')
    serializer_class = ChallengeListSerializer


class PrivateChallengeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(private_public_type='PR')
    serializer_class = ChallengeListSerializer


class PrivateChallengeSportListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='S')
    queryset = queryset.filter(private_public_type='PR')
    serializer_class = ChallengeListSerializer


class PrivateChallengeHealthListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='H')
    queryset = queryset.filter(private_public_type='PR')
    serializer_class = ChallengeListSerializer


class PrivateChallengeLifestyleListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='L')
    queryset = queryset.filter(private_public_type='PR')
    serializer_class = ChallengeListSerializer


class PublicChallengeSportListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='S')
    queryset = queryset.filter(private_public_type='PU')
    serializer_class = ChallengeListSerializer


class PublicChallengeHealthListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='H')
    queryset = queryset.filter(private_public_type='PU')
    serializer_class = ChallengeListSerializer


class PublicChallengeLifestyleListView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all().filter(categories='L')
    queryset = queryset.filter(private_public_type='PU')
    serializer_class = ChallengeListSerializer


class ChallengeListViewForUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChallengeListSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Challenge.objects.filter(owner=user)
        raise PermissionDenied()


class ChallengeDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer


class PrivateChallengeAddView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeAddSerializer


class PublicChallengeAddView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeAddSerializer


class ChallengeUpdateView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer


class ChallengeDeleteView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class FeedbackAddView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackAddSerializer


class JoinPublicChallengeView(viewsets.ModelViewSet):
    queryset = UserChallengeProgress.objects.all()
    serializer_class = JoinPublicChallengeSerializer


class JoinPrivateChallengeView(APIView):

    def post(self, request, format=None):
        try:
            serializer = JoinPrivateChallengeSerializer(data=request.data)

            if serializer.is_valid():
                user_id = serializer.data.get('user_id')
                challenge_id = serializer.data.get('challenge_id')
                password = serializer.data.get('password')
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=user_id)
            challenge = Challenge.objects.get(id=challenge_id)

            if challenge.password == password:
                progress = UserChallengeProgress()
                progress.user = user
                progress.challenge = challenge
                progress.save()

                return Response({'status': 'OK'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Password is not right.'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'status': "Internal Server Error."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
