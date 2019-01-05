from rest_framework import serializers
from .models import Artifact, Artifact_Description,Artifact_Stat

class DescSerializer(serializers.ModelSerializer):
   class Meta:
      model = Artifact_Description
      fields = '__all__'

class StatSerializer(serializers.ModelSerializer):
   class Meta:
      model = Artifact_Stat
      fields = '__all__'

class ArtifactSerializer(serializers.ModelSerializer):
   desc = DescSerializer(many=True, read_only=True)
   stat = StatSerializer(many=True, read_only=True)
 
   class Meta:
      model = Artifact
      fields = ('name','rarity','exclusive','lore_description','desc','stat')