# Generated by Django 4.0.2 on 2022-10-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('projects', '0037_delete_customvessel'), ('wells', '0042_alter_completevesseluse_vessel_and_more')]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='CustomVessel',
                ),
            ],
        )
    ]