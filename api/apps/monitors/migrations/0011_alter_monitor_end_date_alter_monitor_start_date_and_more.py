# Generated by Django 4.0.2 on 2022-07-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0010_remove_monitorelementvalue_baseline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='monitorelementvalue',
            name='date',
            field=models.DateTimeField(),
        ),
    ]