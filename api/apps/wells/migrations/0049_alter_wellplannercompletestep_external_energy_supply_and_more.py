# Generated by Django 4.0.2 on 2022-10-24 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0053_auto_20221024_0923'),
        ('wells', '0048_alter_wellplannercompletestep_external_energy_supply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellplannercompletestep',
            name='external_energy_supply',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.externalenergysupply'
            ),
        ),
        migrations.AlterField(
            model_name='wellplannerplannedstep',
            name='external_energy_supply',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.externalenergysupply'
            ),
        ),
    ]
