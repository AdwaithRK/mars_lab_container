# Generated by Django 4.2.7 on 2023-12-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars', '0012_team_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='status',
            field=models.CharField(choices=[('CURRENT', 'current'), ('ALLUMNI', 'allumni')], default='CURRENT', max_length=8),
        ),
    ]
