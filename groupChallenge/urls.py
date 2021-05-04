from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('challenges/',
         views.ChallengeListView.as_view({'get': 'list'}),
         name='challenges-list'),
    path('challenge/<int:pk>/',
         views.ChallengeDetailView.as_view({'get': 'retrieve'}),
         name='challenge-detail'),
    path('challenge/add/',
         views.ChallengeAddView.as_view({'post': 'create'}),
         name='challenge-add')
])
