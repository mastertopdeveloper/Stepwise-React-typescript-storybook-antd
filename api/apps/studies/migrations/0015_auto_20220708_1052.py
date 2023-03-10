# Generated by Django 4.0.2 on 2022-07-08 10:52

from django.db import migrations

METRICS_DATA = {
    "helicopter_trips": {
        "name": "Total helicopter trips",
        "unit": "",
    },
    "helicopter_fuel": {
        "name": "Total helicopter fuel consumption",
        "unit": "tons",
    },
    "helicopter_co2": {
        "name": "Total helicopter CO2 emission",
        "unit": "tons",
    },
    "helicopter_cost": {
        "name": "Total helicopter cost",
        "unit": "USD",
    },
    "psv_trips": {
        "name": "Total PSV trips",
        "unit": "",
    },
    "psv_fuel": {
        "name": "Total PSV fuel consumption",
        "unit": "tons",
    },
    "psv_cost": {
        "name": "Total PSV cost",
        "unit": "USD",
    },
    "psv_co2": {
        "name": "Total PSV CO2 emission",
        "unit": "tons",
    },
    "cost_per_day": {
        "name": "Day rate",
        "unit": "USD",
    },
    "total_fuel": {
        "name": "Total fuel consumption",
        "unit": "tons",
    },
    "total_cost": {
        "name": "Total cost",
        "unit": "USD",
    },
    "total_co2": {
        "name": "Total CO2 emission",
        "unit": "tons",
    },
    "tugs_cost": {
        "name": "Total tugs cost",
        "unit": "USD",
        "is_jackup_compatible": True,
        "is_semi_compatible": False,
    },
    "ahv_fuel": {
        "name": "Total AHV fuel consumption",
        "unit": "USD",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_logistic_cost": {
        "name": "Total logistic cost",
        "unit": "USD",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_move_cost": {
        "name": "Total move cost",
        "unit": "USD",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_fuel_cost": {
        "name": "Total fuel cost",
        "unit": "USD",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_transit_co2": {
        "name": "Total transit CO2 emission",
        "unit": "tons",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_support_co2": {
        "name": "Total support CO2 emission",
        "unit": "tons",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
    "total_rig_and_spread_cost": {
        "name": "Total rig and spread cost",
        "unit": "USD",
        "is_jackup_compatible": False,
        "is_semi_compatible": True,
    },
}


def create_or_update_study_metrics(apps, _):
    StudyMetricModel = apps.get_model('studies', 'StudyMetric')

    for key, data in METRICS_DATA.items():
        StudyMetricModel.objects.update_or_create(
            key=key,
            defaults={
                "is_jackup_compatible": True,
                "is_semi_compatible": True,
                "is_drillship_compatible": False,
                **data,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0014_studymetric_is_drillship_compatible_and_more'),
    ]

    operations = [migrations.RunPython(create_or_update_study_metrics, migrations.RunPython.noop)]
