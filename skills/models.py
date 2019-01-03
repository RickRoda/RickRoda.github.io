from django.db import models

# Create your models here.
class Skill(models.Model):
	name = models.CharField(max_length=255)
	character = models.ForeignKey(
		'characters.Character',
		related_name = 'skills',
		on_delete=models.CASCADE
		)
	souls_aquired = models.IntegerField(blank=True, null=True)
	turns = models.IntegerField(blank=True,null=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	has_burn = models.BooleanField(default=False)
	burn_consume = models.IntegerField(blank=True,null=True)
	burn_description = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name