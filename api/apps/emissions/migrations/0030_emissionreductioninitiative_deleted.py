# Generated by Django 4.0.2 on 2022-10-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0029_assetreferencematerial_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emissionreductioninitiative',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
