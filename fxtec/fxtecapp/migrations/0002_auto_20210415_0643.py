# Generated by Django 2.2.12 on 2021-04-15 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='Run',
            new_name='run',
        ),
    ]
