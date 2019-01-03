from django.shortcuts import render
from django.views.generic import ListView
from .models import Character
from skills.models import Skill
from .serializers import CharacterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny


class CharacterList(generics.ListCreateAPIView):
	queryset = Character.objects.all()
	serializer_class = CharacterSerializer
	permission_classes = (AllowAny,)
