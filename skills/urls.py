from django.urls import path
from .views import SkillList

urlpatterns = [
	path('', SkillList.as_view()),
	]