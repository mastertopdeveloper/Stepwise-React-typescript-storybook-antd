# Generated by Django 4.0.2 on 2022-09-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0009_baseline_unique_active_baseline'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='baseline',
            constraint=models.CheckConstraint(
                check=models.Q(models.Q(('active', True), ('draft', False)), ('active', False), _connector='OR'),
                name='active_never_draft',
            ),
        ),
    ]
