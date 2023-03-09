# Generated by Django 4.0.2 on 2022-09-12 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_rigplanner_draft'),
        ('wells', '0029_alter_wellplannermode_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellplannermode',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wellplannermode',
            name='rig_planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
        ),
        migrations.AlterField(
            model_name='wellplannerphase',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wellplannerphase',
            name='rig_planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
        ),
        migrations.AlterUniqueTogether(
            name='wellplannermode',
            unique_together={('rig_planner', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='wellplannerphase',
            unique_together={('rig_planner', 'name')},
        ),
    ]
