# Generated by Django 4.0.2 on 2022-10-13 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0040_auto_20221013_1025'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customhelicopter',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='customhelicopter',
            name='helicopter',
        ),
        migrations.DeleteModel(
            name='ConceptHelicopter',
        ),
    ]
