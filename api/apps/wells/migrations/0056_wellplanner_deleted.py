# Generated by Django 4.0.2 on 2022-11-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0055_alter_wellplanner_baseline'),
    ]

    operations = [
        migrations.AddField(
            model_name='wellplanner',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
