from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
   	class Meta:
   		model = Skill
   		fields = (
   			'name',
   			'souls_aquired',
   			'turns',
   			'description',
   			'has_burn',
   			'burn_consume',
   			'burn_description')