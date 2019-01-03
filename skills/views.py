from django.shortcuts import render
from django.views.generic import ListView
from .models import Skill
from .serializers import SkillSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny


class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.prefetch_related('character')
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)
