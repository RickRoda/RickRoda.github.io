from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Artifact
from .serializers import ArtifactSerializer

class ArtifactList(generics.ListCreateAPIView):
	queryset = queryset = Artifact.objects.prefetch_related('skill_description')
	serializer_class = ArtifactSerializer
	permission_classes = (AllowAny,)
