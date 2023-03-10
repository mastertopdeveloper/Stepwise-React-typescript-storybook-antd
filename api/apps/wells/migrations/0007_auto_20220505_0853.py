# Generated by Django 4.0.2 on 2022-05-05 08:53

from django.db import migrations, models


class MetoceanData(models.TextChoices):
    GENERIC_NORTH_SEA = "GENERIC_NORTH_SEA", "Generic North Sea"


class MudType(models.TextChoices):
    OIL_BASED = "OIL_BASED", "Oil based"


def fix_well_data(apps, *args):
    ConceptWell = apps.get_model('wells', 'ConceptWell')
    CustomWell = apps.get_model('wells', 'CustomWell')

    for WellModel in [ConceptWell, CustomWell]:
        WellModel.objects.filter(xt_weight__lt=1).update(xt_weight=1)
        WellModel.objects.update(metocean_data=MetoceanData.GENERIC_NORTH_SEA)
        WellModel.objects.update(intermediate_casing_section_mud_type=MudType.OIL_BASED)
        WellModel.objects.update(production_casing_section_mud_type=MudType.OIL_BASED)
        WellModel.objects.update(extension_section_mud_type=MudType.OIL_BASED)


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0006_remove_conceptwell_area_and_more'),
    ]

    operations = [migrations.RunPython(fix_well_data)]
