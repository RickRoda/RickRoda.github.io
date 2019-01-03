from django.contrib import admin
from .models import Character
from skills.models import Skill
# Register your models here.
class SkillInLine(admin.TabularInline):
    model = Skill


class CharacterAdmin(admin.ModelAdmin):
	inlines = [SkillInLine]

admin.site.register(Character, CharacterAdmin)
