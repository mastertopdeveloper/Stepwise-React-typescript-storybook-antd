# Generated by Django 4.0.2 on 2022-06-13 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_alter_plan_distance_from_tug_base_to_previous_well_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='distance_from_tug_base_to_previous_well',
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
                verbose_name='Distance from Tug base to previous well (nm)',
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_from_previous_location',
            field=models.FloatField(
                help_text='Distance from previous well (nm)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_ahv_base',
            field=models.FloatField(
                help_text='Distance to AHV base (nm)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_helicopter_base',
            field=models.FloatField(
                help_text='Distance to Helicopter base (nm)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_psv_base',
            field=models.FloatField(
                help_text='Distance to PSV base (nm)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='planwellrelation',
            name='distance_to_tug_base',
            field=models.FloatField(
                help_text='Distance to Tug base (nm)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
    ]
