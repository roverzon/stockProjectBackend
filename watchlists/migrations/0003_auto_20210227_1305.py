# Generated by Django 3.1.6 on 2021-02-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlists', '0002_auto_20210227_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlisttosymbol',
            old_name='watchlist_name',
            new_name='watchlist_id',
        ),
        migrations.RemoveField(
            model_name='watchlisttosymbol',
            name='user_id',
        ),
    ]