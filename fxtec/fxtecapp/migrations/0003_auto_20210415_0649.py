# Generated by Django 2.2.12 on 2021-04-15 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0002_auto_20210415_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='contract_expried',
            new_name='contract_expired',
        ),
    ]
