# Generated by Django 4.0.2 on 2022-06-21 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0009_monitorelementvalue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitorelementvalue',
            name='baseline',
        ),
        migrations.RemoveField(
            model_name='monitorelementvalue',
            name='target',
        ),
    ]
