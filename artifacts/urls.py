from django.urls import path
from .views import ArtifactList

urlpatterns = [
	path('', ArtifactList.as_view()),
	] 