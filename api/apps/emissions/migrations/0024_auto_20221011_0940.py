# Generated by Django 4.0.2 on 2022-10-11 09:40

from django.db import migrations


def create_unique_order(apps, _):
    BaselineModel = apps.get_model('emissions', 'Baseline')

    for baseline in BaselineModel.objects.all():
        for index, baseline_input in enumerate(baseline.baselineinput_set.all()):
            baseline_input.order = index
            baseline_input.save()


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0023_baseline_version_baselineinput_order'),
    ]

    operations = [
        migrations.RunPython(create_unique_order, migrations.RunPython.noop),
    ]
