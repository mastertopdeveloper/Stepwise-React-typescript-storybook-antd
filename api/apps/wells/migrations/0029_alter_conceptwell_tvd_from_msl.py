# Generated by Django 4.0.2 on 2022-09-15 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0028_merge_20220913_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptwell',
            name='tvd_from_msl',
            field=models.PositiveIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(20000),
                ],
                verbose_name='TVD from MSL (m)',
            ),
            preserve_default=False,
        ),
    ]
