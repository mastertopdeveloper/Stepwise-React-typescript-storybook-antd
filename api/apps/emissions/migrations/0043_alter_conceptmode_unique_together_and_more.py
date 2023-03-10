# Generated by Django 4.0.2 on 2022-11-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0042_alter_materialtype_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='conceptmode',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='conceptmode',
            name='transit',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conceptphase',
            name='transit',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='conceptmode',
            constraint=models.UniqueConstraint(fields=('tenant', 'name'), name='unique_concept_mode_name'),
        ),
        migrations.AddConstraint(
            model_name='conceptmode',
            constraint=models.UniqueConstraint(
                condition=models.Q(('transit', True)), fields=('tenant', 'transit'), name='unique_concept_mode_transit'
            ),
        ),
        migrations.AddConstraint(
            model_name='conceptphase',
            constraint=models.UniqueConstraint(fields=('tenant', 'name'), name='unique_concept_phase_name'),
        ),
        migrations.AddConstraint(
            model_name='conceptphase',
            constraint=models.UniqueConstraint(
                condition=models.Q(('transit', True)), fields=('tenant', 'transit'), name='unique_concept_phase_transit'
            ),
        ),
    ]
