# Generated by Django 4.0.2 on 2022-09-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_customhelicopter_fuel_cost_customhelicopter_nox_and_more'),
        ('emps', '0015_merge_20220914_0613'),
        ('wells', '0033_merge_20220921_0801'),
        ('studies', '0017_auto_20220915_0855'),
    ]

    database_operations = [migrations.AlterModelTable('rigplanner', 'emissions_asset')]

    operations = [migrations.SeparateDatabaseAndState(database_operations=database_operations, state_operations=[])]
