from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('register/', UserDetailView, name='register')
]