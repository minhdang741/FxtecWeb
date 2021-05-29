# Generated by Django 3.2 on 2021-04-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxtecapp', '0012_alter_robot_account_warning_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='BALANCE',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='BEAR_LEVEL',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='CONTRACT_EXPIRED',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='CURRENCY',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='EQUITY',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='LOGIN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='MARGIN',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='MARGIN_FREE',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='MARGIN_LEVEL',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='N0_OF_LOSS',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='N0_TRUST_WIN',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='PROFIT',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='ROI_LEVEL',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='RUN',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='robot',
            name='TIME',
            field=models.BigIntegerField(),
        ),
    ]