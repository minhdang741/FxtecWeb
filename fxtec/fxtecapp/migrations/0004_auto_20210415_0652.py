# Generated by Django 2.2.12 on 2021-04-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0003_auto_20210415_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='system_alert',
            field=models.CharField(max_length=1),
        ),
    ]
