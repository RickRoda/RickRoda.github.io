from django.urls import path
from .views import CharacterList

urlpatterns = [
	path('', CharacterList.as_view()),
	]