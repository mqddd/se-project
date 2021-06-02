from django.urls import path
from .views import UserDetial
urlpatterns = [
    path("<int:pk>" , UserDetial.as_view(), name='UserDetail' ),
]