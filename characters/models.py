from django.db import models
from django.contrib import admin

class Character(models.Model):
	#General Character Info
	name = models.CharField(max_length=255)
	role = models.CharField(max_length=32)
	zodiac_sign = models.CharField(max_length=32)
	stars = models.IntegerField()

	#Character Stats
	attack = models.IntegerField()
	defense = models.IntegerField()
	health = models.IntegerField()
	speed = models.IntegerField()
	crit_chance = models.FloatField()
	crit_damage = models.FloatField()
	effectiveness = models.FloatField()
	effect_resistance = models.FloatField()
	dual_atk_chance = models.FloatField()

	def __str__(self):
		return self.name


