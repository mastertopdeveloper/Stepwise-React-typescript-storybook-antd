# Generated by Django 4.0.2 on 2022-12-15 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0066_targetco2_targetco2reduction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baselineco2',
            options={'verbose_name': 'Baseline CO2'},
        ),
        migrations.AlterModelOptions(
            name='targetco2',
            options={'verbose_name': 'Target CO2'},
        ),
        migrations.AlterModelOptions(
            name='targetco2reduction',
            options={'verbose_name': 'Target CO2 reduction'},
        ),
    ]
