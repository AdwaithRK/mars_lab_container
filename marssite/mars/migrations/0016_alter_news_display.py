# Generated by Django 4.2.7 on 2023-12-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars', '0015_news_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='display',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='NO', max_length=8),
        ),
    ]
