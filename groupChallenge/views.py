from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *


class AllChallengesApiView(APIView):

    def get(self, request, format=None):
        try:
            challenges = Challenge.objects.all()
            data = []

            for challenge in challenges:
                data.append(
                    {
                        "title": challenge.title,
                        "desc": challenge.description,
                    }
                )

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'error occurred'}, status=status.HTTP_400_BAD_REQUEST)
