# Register your models here.
from django.contrib import admin
from .models import Artifact, Artifact_Description,Artifact_Stat
from skills.models import Skill
# Register your models here.
class DescInLine(admin.TabularInline):
    model = Artifact_Description
class StatsInLine(admin.TabularInline):
    model = Artifact_Stat

class ArtifactAdmin(admin.ModelAdmin):
	inlines = [DescInLine, StatsInLine]

admin.site.register(Artifact, ArtifactAdmin)