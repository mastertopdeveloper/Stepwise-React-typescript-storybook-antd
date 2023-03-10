# Generated by Django 4.0.2 on 2022-10-13 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0022_rename_fuel_helicoptertype_fuel_consumption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helicoptertype',
            name='nox',
        ),
        migrations.AddField(
            model_name='helicoptertype',
            name='co2_per_fuel',
            field=models.FloatField(
                default=0, help_text='Ton CO2/m3 fuel', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helicoptertype',
            name='co2_tax',
            field=models.FloatField(
                default=0, help_text='CO2 tax (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helicoptertype',
            name='fuel_density',
            field=models.FloatField(
                default=0, help_text='Fuel density (kg/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helicoptertype',
            name='nox_per_fuel',
            field=models.FloatField(
                default=0, help_text='kg NOx/m3 fuel', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helicoptertype',
            name='nox_tax',
            field=models.FloatField(
                default=0, help_text='NOx tax (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='helicoptertype',
            name='fuel_cost',
            field=models.FloatField(
                help_text='Fuel cost (USD/m3)', validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name='helicoptertype',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
