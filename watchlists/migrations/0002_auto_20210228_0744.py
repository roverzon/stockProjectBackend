# Generated by Django 3.1.6 on 2021-02-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='symbol_cnt',
            field=models.IntegerField(default=1),
        ),
    ]