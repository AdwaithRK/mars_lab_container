# Generated by Django 4.2.7 on 2023-11-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.TextField()),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]