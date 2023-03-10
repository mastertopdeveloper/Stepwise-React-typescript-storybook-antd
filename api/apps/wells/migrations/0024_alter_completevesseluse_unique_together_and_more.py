# Generated by Django 4.0.2 on 2022-09-08 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_rigplanner_draft'),
        ('wells', '0023_alter_wellplanner_current_step'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='completevesseluse',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='plannedvesseluse',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='completevesseluse',
            name='season',
            field=models.CharField(
                choices=[('SUMMER', 'Summer'), ('WINTER', 'Winter')], default='SUMMER', max_length=16
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plannedvesseluse',
            name='season',
            field=models.CharField(
                choices=[('SUMMER', 'Summer'), ('WINTER', 'Winter')], default='SUMMER', max_length=16
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plannedvesseluse',
            name='waiting_on_weather',
            field=models.FloatField(
                default=10,
                help_text='Waiting on weather contingency (%)',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='completevesseluse',
            unique_together={('well_planner', 'vessel', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='plannedvesseluse',
            unique_together={('well_planner', 'vessel', 'season')},
        ),
    ]
