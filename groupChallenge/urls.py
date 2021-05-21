from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('challenges/',
         views.ChallengeListView.as_view({'get': 'list'}),
         name='challenge-list'),
    path('challenge/<int:pk>/',
         views.ChallengeDetailView.as_view({'get': 'retrieve'}),
         name='challenge-detail'),
    path('challenge/add/',
         views.ChallengeAddView.as_view({'post': 'create'}),
         name='challenge-add'),
    path('challenge/<int:pk>/update',
         views.ChallengeUpdateView.as_view({'post': 'update'}),
         name='challenge-update'),
    path('challenge/<int:pk>/delete',
         views.ChallengeDeleteView.as_view({'post': 'destroy'}),
         name='challenge-delete'),
    path('feedback/add/',
         views.FeedbackAddView.as_view({'post': 'create'}),
         name='feedback-add'),
    # test paths
    path('user/<int:pk>',
         views.UserDetailView.as_view({'get': 'retrieve'}),
         name='user-detail')
])
