# Generated by Django 4.0.2 on 2022-10-05 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0018_wellplannermode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WellPlannerMode',
            new_name='CustomMode',
        ),
    ]
