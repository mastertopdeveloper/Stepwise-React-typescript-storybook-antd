# Generated by Django 4.0.2 on 2022-08-16 10:02

from django.db import migrations, models

import apps.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0017_alter_completehelicopteruse_trips_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completehelicopteruse',
            name='fuel',
            field=models.FloatField(
                help_text='Fuel consumption per hour in liters',
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='completehelicopteruse',
            name='trip_duration',
            field=models.FloatField(
                help_text='Duration of a roundtrip flight', validators=[apps.core.validators.GreaterThanValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='plannedhelicopteruse',
            name='fuel',
            field=models.FloatField(
                help_text='Fuel consumption per hour in liters',
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='plannedhelicopteruse',
            name='trip_duration',
            field=models.FloatField(
                help_text='Duration of a roundtrip flight', validators=[apps.core.validators.GreaterThanValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='cement_volume',
            field=models.FloatField(
                blank=True,
                help_text='Volume of cement in cubic meters',
                null=True,
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='duration',
            field=models.FloatField(
                help_text='Phase duration in days', validators=[apps.core.validators.GreaterThanValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='steel_weight',
            field=models.FloatField(
                blank=True,
                help_text='Weight of steel in mT',
                null=True,
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='cement_volume',
            field=models.FloatField(
                blank=True,
                help_text='Volume of cement in cubic meters',
                null=True,
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='duration',
            field=models.FloatField(
                help_text='Phase duration in days', validators=[apps.core.validators.GreaterThanValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='steel_weight',
            field=models.FloatField(
                blank=True,
                help_text='Weight of steel in mT',
                null=True,
                validators=[apps.core.validators.GreaterThanValidator(0)],
            ),
        ),
    ]
