from django.shortcuts import render
from characters.models import Character
from skills.models import Skill

def index(request):
	num_of_chars = Character.objects.all().count()
	num_of_skills = Skill.objects.all().count()

	context = {
	'num_chars_added' : num_of_chars,
	'num_skills_added' : num_of_skills,
	}

	return render(request,'index.html',context = context)
