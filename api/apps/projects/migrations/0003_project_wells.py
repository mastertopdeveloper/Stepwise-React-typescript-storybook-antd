# Generated by Django 4.0.2 on 2022-03-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0003_customwell'),
        ('projects', '0002_project_jackup_rigs_project_semi_rigs'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='wells',
            field=models.ManyToManyField(blank=True, to='wells.CustomWell'),
        ),
    ]
