# Generated by Django 4.0.2 on 2022-11-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0057_auto_20221124_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wellplanner',
            name='type',
        ),
        migrations.AlterField(
            model_name='wellplanner',
            name='side_track',
            field=models.CharField(max_length=255),
        ),
    ]
