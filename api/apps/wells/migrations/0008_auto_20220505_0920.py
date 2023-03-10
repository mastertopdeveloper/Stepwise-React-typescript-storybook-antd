# Generated by Django 4.0.2 on 2022-05-05 09:20

from django.db import migrations


def fix_metocean_days_above_hs_5(apps, *args):
    ConceptWell = apps.get_model('wells', 'ConceptWell')
    CustomWell = apps.get_model('wells', 'CustomWell')

    for WellModel in [ConceptWell, CustomWell]:
        WellModel.objects.update(metocean_days_above_hs_5=0)


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0007_auto_20220505_0853'),
    ]

    operations = [migrations.RunPython(fix_metocean_days_above_hs_5)]
