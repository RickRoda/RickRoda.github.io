# Generated by Django 2.1.4 on 2019-01-03 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20190103_1657'),
        ('characters', '0004_remove_character_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_skills', to='skills.Skill'),
        ),
    ]
