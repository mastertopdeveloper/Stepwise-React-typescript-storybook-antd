# Generated by Django 4.0.2 on 2022-10-05 20:52

from django.db import migrations

MODE_NAMES = (
    'Transit / Stand by',
    'Pos moore',
    'Dynamic positioning',
    'Anchor',
)


def create_concept_modes(apps, _):
    TenantModel = apps.get_model('tenants', 'Tenant')
    ConceptModeModel = apps.get_model('emissions', 'ConceptMode')
    CustomModeModel = apps.get_model('emissions', 'CustomMode')

    for tenant in TenantModel.objects.all():
        for name in MODE_NAMES:
            concept_well_planner_mode, _ = ConceptModeModel.objects.get_or_create(
                tenant=tenant,
                name=name,
                description=f"{name} mode",
            )
            CustomModeModel.objects.filter(
                asset__tenant=tenant,
                name=name,
            ).update(mode=concept_well_planner_mode, description=f"{name} mode")


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0021_custommode_description_and_more'),
    ]

    operations = [migrations.RunPython(create_concept_modes, migrations.RunPython.noop)]
