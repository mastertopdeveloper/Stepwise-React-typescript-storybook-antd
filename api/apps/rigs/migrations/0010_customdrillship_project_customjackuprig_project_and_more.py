# Generated by Django 4.0.2 on 2022-05-24 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_project_wells'),
        ('rigs', '0009_auto_20220523_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='customdrillship',
            name='project',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'
            ),
        ),
        migrations.AddField(
            model_name='customjackuprig',
            name='project',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'
            ),
        ),
        migrations.AddField(
            model_name='customsemirig',
            name='project',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'
            ),
        ),
    ]
