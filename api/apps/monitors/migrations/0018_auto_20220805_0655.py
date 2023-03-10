# Generated by Django 4.0.2 on 2022-08-05 06:55

from django.db import migrations


def migrate_monitor_functions(apps, *args):
    MonitorFunction = apps.get_model('monitors', 'MonitorFunction')
    MonitorElement = apps.get_model('monitors', 'MonitorElement')
    MonitorElementValue = apps.get_model('monitors', 'MonitorElementValue')

    for monitor_element in MonitorElement.objects.select_related('monitor__vessel').all():
        start_date = monitor_element.created_at.replace(minute=0, second=0, microsecond=0)
        monitor_function = MonitorFunction.objects.create(
            name=monitor_element.name,
            draft=monitor_element.draft,
            monitor_function_source=monitor_element.monitor_function_source,
            vessel=monitor_element.monitor.vessel,
            start_date=start_date,
        )
        monitor_element.monitor_function = monitor_function
        monitor_element.save()
        MonitorElementValue.objects.filter(monitor_element=monitor_element).update(monitor_function=monitor_function)


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0017_monitorfunction_monitorelement_monitor_function_and_more'),
    ]

    operations = [migrations.RunPython(migrate_monitor_functions)]
