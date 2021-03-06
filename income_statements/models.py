from django.db import models


class Income(models.Model):
    symbol = models.CharField(max_length=255, blank=False, default='')
    report_type = models.CharField(max_length=255, blank=False, default='')
    fiscal_date_ending = models.DateTimeField()
    fiscal_year = models.CharField(max_length=10)
    reported_currency = models.CharField(max_length=10)
    total_revenue = models.FloatField()
    total_operating_expense = models.FloatField()
    cost_of_revenue = models.FloatField()
    gross_profit = models.FloatField()
    ebit = models.FloatField()
    net_income = models.FloatField()
    research_and_development = models.FloatField()
    effect_of_accounting_charges = models.FloatField()
    income_before_tax = models.FloatField()
    minority_interest = models.FloatField()
    selling_general_administrative = models.FloatField()
    other_non_operating_income = models.FloatField()
    operating_income = models.FloatField()
    other_operating_expense = models.FloatField()
    interest_expense = models.FloatField()
    tax_provision = models.FloatField()
    interest_income = models.FloatField()
    net_interest_income = models.FloatField()
    extraordinary_items = models.FloatField()
    non_recurring = models.FloatField()
    other_items = models.FloatField()
    income_tax_expense = models.FloatField()
    total_other_income_expense = models.FloatField()
    discontinued_operations = models.FloatField()
    net_income_from_continuing_operations = models.FloatField()
    net_income_applicable_to_common_shares = models.FloatField()
    preferred_stock_and_other_adjustments = models.FloatField()