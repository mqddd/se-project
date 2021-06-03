from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserDetailView

urlpatterns = format_suffix_patterns([
    path('update/<int:pk>/',
         UserDetailView.as_view({'post': 'update'}),
         name='user-update'),
])
