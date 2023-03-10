# Generated by Django 4.0.2 on 2022-06-14 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_project_tugs_avg_fuel_consumption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planwellrelation',
            name='jackup_positioning_time',
            field=models.FloatField(
                help_text='Jackup positioning time (d)',
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='semi_positioning_time',
            field=models.FloatField(
                help_text='Semi positioning time (d)',
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='helicopter_cruise_speed',
            field=models.FloatField(
                help_text='Cruise speed (kn)',
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='psv_avg_fuel_dp_consumption',
            field=models.FloatField(
                help_text='Average PSV fuel DP consumption (t/d)',
                validators=[
                    django.core.validators.MinValueValidator(0.1),
                    django.core.validators.MaxValueValidator(30),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='psv_avg_fuel_transit_consumption',
            field=models.FloatField(
                help_text='Average PSV fuel transit consumption (t/d)',
                validators=[
                    django.core.validators.MinValueValidator(0.1),
                    django.core.validators.MaxValueValidator(50),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='psv_loading_time',
            field=models.FloatField(
                help_text='PSV loading time (d)',
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='psv_speed',
            field=models.FloatField(
                help_text='PSV speed (kn)',
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='tugs_avg_move_fuel_consumption',
            field=models.FloatField(
                help_text='Average Tug move fuel consumption (t/d)',
                validators=[
                    django.core.validators.MinValueValidator(0.1),
                    django.core.validators.MaxValueValidator(30),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='tugs_avg_transit_fuel_consumption',
            field=models.FloatField(
                help_text='Average Tug transit fuel consumption (t/d)',
                validators=[
                    django.core.validators.MinValueValidator(0.1),
                    django.core.validators.MaxValueValidator(30),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='tugs_move_speed',
            field=models.FloatField(
                help_text='Tug move speed (kn)',
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='tugs_transit_speed',
            field=models.FloatField(
                help_text='Tug transit speed (kn)',
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(40)],
            ),
        ),
    ]
