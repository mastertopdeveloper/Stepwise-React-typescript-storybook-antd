# Generated by Django 4.0.2 on 2022-10-24 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0050_auto_20221024_0824'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customexternalsupply',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='customexternalsupply',
            name='external_supply',
        ),
        migrations.DeleteModel(
            name='ConceptExternalSupply',
        ),
    ]
