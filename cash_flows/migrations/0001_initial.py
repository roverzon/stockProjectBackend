# Generated by Django 3.1.6 on 2021-02-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='', max_length=10)),
                ('report_type', models.CharField(default='', max_length=255)),
                ('reported_currency', models.CharField(default='USD', max_length=255)),
                ('fiscal_date_ending', models.DateTimeField(default='1900-01-01')),
                ('investments', models.FloatField(default=0.0)),
                ('change_in_liabilities', models.FloatField(default=0.0)),
                ('cashflow_from_investment', models.FloatField(default=0.0)),
                ('other_cashflow_from_investment', models.FloatField(default=0.0)),
                ('net_borrowings', models.FloatField(default=0.0)),
                ('cashflow_from_financing', models.FloatField(default=0.0)),
                ('other_cashflow_from_financing', models.FloatField(default=0.0)),
                ('change_in_operating_activities', models.FloatField(default=0.0)),
                ('net_income', models.FloatField(default=0.0)),
                ('change_in_cash', models.FloatField(default=0.0)),
                ('operating_cashflow', models.FloatField(default=0.0)),
                ('other_operating_cashflow', models.FloatField(default=0.0)),
                ('depreciation', models.FloatField(default=0.0)),
                ('dividend_payout', models.FloatField(default=0.0)),
                ('stock_sale_and_purchase', models.FloatField(default=0.0)),
                ('change_in_inventory', models.FloatField(default=0.0)),
                ('change_in_account_receivables', models.FloatField(default=0.0)),
                ('change_in_net_income', models.FloatField(default=0.0)),
                ('capital_expenditures', models.FloatField(default=0.0)),
                ('change_in_receivables', models.FloatField(default=0.0)),
                ('change_in_exchange_rate', models.FloatField(default=0.0)),
                ('change_in_cash_and_cash_equivalents', models.FloatField(default=0.0)),
            ],
        ),
    ]
