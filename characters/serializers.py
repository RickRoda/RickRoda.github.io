from rest_framework import serializers
from .models import Character
from skills.serializers import SkillSerializer

class CharacterSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = (
        	'name',
        	'role',
        	'zodiac_sign',
        	'stars',
        	'attack',
        	'defense',
        	'health',
        	'speed',
        	'crit_chance',
        	'crit_damage',
        	'effectiveness',
        	'effect_resistance',
        	'dual_atk_chance',
        	'skills',

        	)