from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^challenges/$', views.AllChallengesApiView.as_view(), name='challenges'),
]
