from django.contrib import admin
from .models import Skill
# Register your models here.
class SkillAdmin(admin.ModelAdmin):
	list_display = ('character', 'name')

admin.site.register(Skill, SkillAdmin)