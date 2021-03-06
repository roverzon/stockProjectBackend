# Generated by Django 3.1.6 on 2021-03-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('market', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('currency_name', models.CharField(max_length=100)),
                ('cik', models.CharField(max_length=100)),
                ('composite_figi', models.CharField(max_length=100)),
                ('share_class_figi', models.CharField(max_length=100)),
                ('last_updated_utc', models.DateTimeField()),
            ],
        ),
    ]
