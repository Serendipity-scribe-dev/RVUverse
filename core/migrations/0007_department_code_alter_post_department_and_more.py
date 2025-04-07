# Generated by Django 5.2 on 2025-04-04 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='code',
            field=models.CharField(choices=[('1', 'School of Liberal Arts and Sciences (SOLAS)'), ('2', 'School of Design and Innovation (SODI)'), ('3', 'School of Business (SOB)'), ('4', 'School of Economics and Public Policy (SOEPP)'), ('5', 'School of Computer Science and Engineering (SOCSE)'), ('6', 'School of Law (SOL)'), ('7', 'School of Film, Media and Creative Arts (SOFMCA)'), ('8', 'School of Continuing Education & Professional Studies (SOCEPS)'), ('9', 'School of Allied and Healthcare Professions (SOAHP)'), ('10', 'None')], default='10', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='core.department'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='core.department'),
        ),
    ]
