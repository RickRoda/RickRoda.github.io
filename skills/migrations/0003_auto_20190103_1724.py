# Generated by Django 2.1.4 on 2019-01-03 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20190103_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='burn_consume',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='turns',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
