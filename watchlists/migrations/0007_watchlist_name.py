# Generated by Django 3.1.6 on 2021-02-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlists', '0006_auto_20210227_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='name',
            field=models.CharField(blank=True, default='watchlist_0', max_length=100),
        ),
    ]