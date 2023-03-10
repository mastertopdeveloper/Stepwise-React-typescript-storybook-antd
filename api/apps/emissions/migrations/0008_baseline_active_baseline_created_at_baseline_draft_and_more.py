# Generated by Django 4.0.2 on 2022-09-28 08:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0007_rename_customenergyuse_baseline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseline',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseline',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseline',
            name='draft',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseline',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='baseline',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.asset'),
        ),
        migrations.AlterField(
            model_name='baselineinput',
            name='baseline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.baseline'),
        ),
    ]
