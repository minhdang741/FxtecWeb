# Generated by Django 2.2.12 on 2021-04-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0004_auto_20210415_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='eqtcheck',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]