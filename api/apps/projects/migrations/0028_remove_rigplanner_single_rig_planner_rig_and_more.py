# Generated by Django 4.0.2 on 2022-08-05 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kims', '0008_tagvalue_average'),
        ('projects', '0027_conceptcarboncapturestoragesystem_conceptcement_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rigplanner',
            name='single_rig_planner_rig',
        ),
        migrations.RemoveField(
            model_name='rigplanner',
            name='custom_drillship',
        ),
        migrations.RemoveField(
            model_name='rigplanner',
            name='custom_jackup_rig',
        ),
        migrations.RemoveField(
            model_name='rigplanner',
            name='custom_semi_rig',
        ),
        migrations.AddField(
            model_name='rigplanner',
            name='vessel',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kims.vessel'
            ),
        ),
    ]
