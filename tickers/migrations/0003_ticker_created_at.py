# Generated by Django 3.1.6 on 2021-03-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickers', '0002_auto_20210306_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='created_at',
            field=models.DateTimeField(default='1900-01-01'),
        ),
    ]