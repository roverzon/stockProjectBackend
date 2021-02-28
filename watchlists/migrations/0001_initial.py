# Generated by Django 3.1.6 on 2021-02-27 08:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('watchlist_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
