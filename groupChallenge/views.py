from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from . import serializers


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


class CreateChallengeApiView(APIView):

    def post(self, request, format=None):
        try:
            serializer_challenge = serializers.createChallengeSerializer(data=request.data)
            if serializer_challenge.is_valid():
                title = serializer_challenge.data.get('title')
                description = serializer_challenge.data.get('description')
                repetition = serializer_challenge.data.get('repetition')
                start_date = serializer_challenge.data.get('start_date')
                end_date = serializer_challenge.data.get('end_date')
                progress_type = serializer_challenge.data.get('progress_type')
                icon = request.FILES['icon']
                private_public_type = serializer_challenge.data.get('private_public_type')
                category_id = serializer_challenge.data.get('category_id')
                owner_id = serializer_challenge.data.get('owner_id')
            else:
                return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

            category = Category.objects.get(id=category_id)
            owner = User.objects.get(id=owner_id)

            challenge = Challenge()

            challenge.title = title
            challenge.description = description
            challenge.repetition = repetition
            challenge.start_date = start_date
            challenge.end_date = end_date
            challenge.progress_type = progress_type
            challenge.icon = icon
            challenge.private_public_type = private_public_type
            challenge.category = category
            challenge.owner = owner

            challenge.save()

        except:
            return Response({'error': 'error occurred'}, status=status.HTTP_400_BAD_REQUEST)
