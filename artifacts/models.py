from django.db import models

# Create your models here.
class Artifact(models.Model):
	name = models.CharField(max_length=255)
	rarity = models.IntegerField()
	exclusive = models.CharField(max_length=255)
	lore_description = models.CharField(max_length=255)
	skill_description = models.ForeignKey(
		'Artifact_Description',
		related_name='artifact_description',
		on_delete=models.CASCADE,
		blank=True,
		null=True)
	stats = models.ForeignKey(
		'Artifact_Stat',
		related_name='artifact_stats',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		)

class Artifact_Description(models.Model):
	artifact = models.ForeignKey(
	'artifacts.Artifact',
	related_name = 'artifact_description',
	on_delete=models.CASCADE
	)
	base = models.CharField(max_length=255)
	maximum = models.CharField(max_length=255)

class Artifact_Stat(models.Model):
	artifact = models.ForeignKey(
	'artifacts.Artifact',
	related_name = 'artifact_stat',
	on_delete=models.CASCADE
	)
	base_attack = models.IntegerField()
	base_hp = models.IntegerField()
	max_attack = models.IntegerField()
	max_hp = models.IntegerField()