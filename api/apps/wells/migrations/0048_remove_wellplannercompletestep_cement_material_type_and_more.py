# Generated by Django 4.0.2 on 2022-10-27 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0031_materialtype'),
        ('wells', '0047_wellplannercompletestep_cement_material_type_and_more'),
        ('projects', '0049_auto_20221026_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='cement',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='steel',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='cement',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='steel',
        ),
        migrations.RenameField(
            model_name='wellplannerplannedstep',
            old_name='cement_material_type',
            new_name='cement',
        ),
        migrations.RenameField(
            model_name='wellplannerplannedstep',
            old_name='steel_material_type',
            new_name='steel',
        ),
        migrations.RenameField(
            model_name='wellplannercompletestep',
            old_name='cement_material_type',
            new_name='cement',
        ),
        migrations.RenameField(
            model_name='wellplannercompletestep',
            old_name='steel_material_type',
            new_name='steel',
        ),
    ]
