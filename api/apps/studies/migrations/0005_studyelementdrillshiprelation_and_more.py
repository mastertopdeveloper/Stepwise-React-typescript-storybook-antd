# Generated by Django 4.0.2 on 2022-05-19 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0008_conceptdrillship_and_more'),
        ('studies', '0004_study'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyElementDrillshipRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveConstraint(
            model_name='studyelementjackuprigrelation',
            name='unique_study_element_jackup_rig_relation',
        ),
        migrations.RemoveConstraint(
            model_name='studyelementsemirigrelation',
            name='unique_study_element_semi_rig_relation',
        ),
        migrations.AddField(
            model_name='studyelement',
            name='drillships',
            field=models.ManyToManyField(
                blank=True, through='studies.StudyElementDrillshipRelation', to='rigs.CustomDrillship'
            ),
        ),
        migrations.AddConstraint(
            model_name='studyelementjackuprigrelation',
            constraint=models.UniqueConstraint(
                fields=('study_element', 'rig'), name='unique_studies_studyelementjackuprigrelation'
            ),
        ),
        migrations.AddConstraint(
            model_name='studyelementsemirigrelation',
            constraint=models.UniqueConstraint(
                fields=('study_element', 'rig'), name='unique_studies_studyelementsemirigrelation'
            ),
        ),
        migrations.AddField(
            model_name='studyelementdrillshiprelation',
            name='rig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rigs.customdrillship'),
        ),
        migrations.AddField(
            model_name='studyelementdrillshiprelation',
            name='study_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.studyelement'),
        ),
        migrations.AddConstraint(
            model_name='studyelementdrillshiprelation',
            constraint=models.UniqueConstraint(
                fields=('study_element', 'rig'), name='unique_studies_studyelementdrillshiprelation'
            ),
        ),
    ]