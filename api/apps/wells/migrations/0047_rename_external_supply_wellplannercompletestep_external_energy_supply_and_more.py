# Generated by Django 4.0.2 on 2022-10-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0046_alter_completehelicopteruse_helicopter_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wellplannercompletestep',
            old_name='external_supply',
            new_name='external_energy_supply',
        ),
        migrations.RenameField(
            model_name='wellplannerplannedstep',
            old_name='external_supply',
            new_name='external_energy_supply',
        ),
    ]