# Generated by Django 4.0.2 on 2022-05-09 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('api_description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_rig_baseline_average', models.FloatField()),
                ('total_rig_target_average', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='conceptempelement',
            old_name='sub_area',
            new_name='subarea',
        ),
        migrations.RenameField(
            model_name='conceptempelement',
            old_name='sub_area_external_id',
            new_name='subarea_external_id',
        ),
        migrations.RenameField(
            model_name='conceptempelement',
            old_name='sub_area_sensors',
            new_name='subarea_sensors',
        ),
        migrations.AddField(
            model_name='conceptempelement',
            name='percentage_improvement',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CustomEMPElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('baseline_average', models.FloatField()),
                ('target_average', models.FloatField()),
                (
                    'concept_emp_element',
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emps.conceptempelement'),
                ),
                (
                    'emp',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='emps.emp'
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
