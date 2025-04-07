# Generated by Django 5.2 on 2025-04-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.CharField(blank=True, choices=[('1', 'School of Liberal Arts and Sciences(SOLAS)'), ('2', 'School of Design and Innovation(SODI)'), ('3', 'School of Business(SOB)'), ('4', 'School of Economics and Public Policy(SOEPP)'), ('5', 'School of Computer Science and Engineering(SOCSE)'), ('6', 'School of Law(SOL)'), ('7', 'School of Film, Media and Creative Arts(SOFMCA)'), ('8', 'School of Continuing Education & Professional Studies(SOCEPS)'), ('9', 'School of Allied and Healthcare Professions(SOAHP)')], max_length=2, null=True),
        ),
    ]
