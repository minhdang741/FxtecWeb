# Generated by Django 3.2 on 2021-04-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0011_auto_20210424_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='ACCOUNT_WARNING_LEVEL',
            field=models.IntegerField(),
        ),
    ]
