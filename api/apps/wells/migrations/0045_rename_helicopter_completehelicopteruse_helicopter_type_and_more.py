# Generated by Django 4.0.2 on 2022-10-13 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0042_rename_customhelicopter_helicoptertype'),
        ('wells', '0044_alter_completevesseluse_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completehelicopteruse',
            old_name='helicopter',
            new_name='helicopter_type',
        ),
        migrations.RenameField(
            model_name='plannedhelicopteruse',
            old_name='helicopter',
            new_name='helicopter_type',
        ),
        migrations.AlterUniqueTogether(
            name='completehelicopteruse',
            unique_together={('well_planner', 'helicopter_type')},
        ),
        migrations.AlterUniqueTogether(
            name='plannedhelicopteruse',
            unique_together={('well_planner', 'helicopter_type')},
        ),
    ]
