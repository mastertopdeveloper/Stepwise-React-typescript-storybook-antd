# Generated by Django 4.0.2 on 2022-11-14 09:07
import random

from django.db import migrations


def get_random_name(*, old_name, asset, Baseline):
    while True:
        number = random.randint(1, 99999)
        new_name = f'{old_name[:250]}{number}'
        if not Baseline.objects.filter(name=new_name, deleted=False, asset=asset).exists():
            return new_name


def migrate_baseline_name(apps, *args):
    Baseline = apps.get_model('emissions', 'Baseline')
    for baseline in Baseline.objects.filter(deleted=False).select_related('asset').order_by('id'):
        if (
            Baseline.objects.filter(
                deleted=False,
                name=baseline.name,
                asset=baseline.asset,
            )
            .exclude(pk=baseline.pk)
            .exists()
        ):
            baseline.name = get_random_name(
                old_name=baseline.name,
                asset=baseline.asset,
                Baseline=Baseline,
            )
            baseline.save()


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0049_emissionmanagementplan_created_at_and_more'),
    ]

    operations = [migrations.RunPython(migrate_baseline_name)]
