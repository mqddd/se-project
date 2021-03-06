from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('public-challenges/',
         views.PublicChallengeListView.as_view({'get': 'list'}),
         name='public-challenge-list'),
    path('private-challenges/',
         views.PrivateChallengeListView.as_view({'get': 'list'}),
         name='private-challenge-list'),
    path('private-challenges-sport/',
         views.PrivateChallengeSportListView.as_view({'get': 'list'}),
         name='private-challenge-list-sport'),
    path('private-challenges-health/',
         views.PrivateChallengeHealthListView.as_view({'get': 'list'}),
         name='private-challenge-list-health'),
    path('private-challenges-lifestyle/',
         views.PrivateChallengeLifestyleListView.as_view({'get': 'list'}),
         name='private-challenge-list-lifestyle'),
    path('public-challenges-sport/',
         views.PublicChallengeSportListView.as_view({'get': 'list'}),
         name='public-challenge-list-sport'),
    path('public-challenges-health/',
         views.PublicChallengeHealthListView.as_view({'get': 'list'}),
         name='public-challenge-list-health'),
    path('public-challenges-lifestyle/',
         views.PublicChallengeLifestyleListView.as_view({'get': 'list'}),
         name='public-challenge-list-lifestyle'),
    path('my-challenges/',
         views.ChallengeListViewForUser.as_view({'get': 'list'}),
         name='my-challenge-list'),
    path('challenge/<int:pk>/',
         views.ChallengeDetailView.as_view({'get': 'retrieve'}),
         name='challenge-detail'),
    path('private-challenge/add/',
         views.PrivateChallengeAddView.as_view({'post': 'create'}),
         name='private-challenge-add'),
    path('public-challenge/add/',
         views.PublicChallengeAddView.as_view({'post': 'create'}),
         name='public-challenge-add'),
    path('challenge/<int:pk>/update',
         views.ChallengeUpdateView.as_view({'post': 'update'}),
         name='challenge-update'),
    path('challenge/<int:pk>/delete',
         views.ChallengeDeleteView.as_view({'post': 'destroy'}),
         name='challenge-delete'),
    path('feedback/add/',
         views.FeedbackAddView.as_view({'post': 'create'}),
         name='feedback-add'),
    path('join-public-challenge/',
         views.JoinPublicChallengeView.as_view({'post': 'create'}),
         name='join-public-challenge'),
    path('join-private-challenge/',
         views.JoinPrivateChallengeView.as_view(),
         name='join-private-challenge'),
])
