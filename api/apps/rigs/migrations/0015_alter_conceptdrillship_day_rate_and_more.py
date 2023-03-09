# Generated by Django 4.0.2 on 2022-06-14 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0014_conceptdrillship_day_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptdrillship',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptdrillship',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptjackuprig',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptjackuprig',
            name='jack_down_time',
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
                verbose_name='Jack down to move time (d)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptjackuprig',
            name='jack_up_time',
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
                verbose_name='Jack up time (d)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptjackuprig',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptsemirig',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='conceptsemirig',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
        migrations.AlterField(
            model_name='customdrillship',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='customdrillship',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
        migrations.AlterField(
            model_name='customjackuprig',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='customjackuprig',
            name='jack_down_time',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
                verbose_name='Jack down to move time (d)',
            ),
        ),
        migrations.AlterField(
            model_name='customjackuprig',
            name='jack_up_time',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)],
                verbose_name='Jack up time (d)',
            ),
        ),
        migrations.AlterField(
            model_name='customjackuprig',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
        migrations.AlterField(
            model_name='customsemirig',
            name='day_rate',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Day rate (USD/d)',
            ),
        ),
        migrations.AlterField(
            model_name='customsemirig',
            name='spread_cost',
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name='Spread cost (USD)',
            ),
        ),
    ]