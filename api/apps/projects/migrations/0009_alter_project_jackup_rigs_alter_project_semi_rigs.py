# Generated by Django 4.0.2 on 2022-05-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0007_customjackuprig_emp_customsemirig_emp'),
        ('projects', '0008_merge_20220505_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='jackup_rigs',
            field=models.ManyToManyField(blank=True, related_name='projects', to='rigs.CustomJackupRig'),
        ),
        migrations.AlterField(
            model_name='project',
            name='semi_rigs',
            field=models.ManyToManyField(blank=True, related_name='projects', to='rigs.CustomSemiRig'),
        ),
    ]
