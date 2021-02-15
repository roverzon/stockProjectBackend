from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from income_statements.models import Income
from income_statements.serializers import IncomeSerializer
from rest_framework.decorators import api_view

from alpha_vantage.fundamentaldata import FundamentalData
from datetime import datetime


@api_view(['GET'])
def income_list(request):
    if request.method == 'GET':
        incomes = Income.objects.all()
        income_serializer = IncomeSerializer(incomes, many=True)
        return JsonResponse(income_serializer.data, safe=False, )

    elif request.method == 'DELETE':
        count = Income.objects.all().delete()
        return JsonResponse({'message': '{} Companies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def symbol_income_list(request, symbol):
    if request.method == 'GET':
        incomes = Income.objects.all()

        if symbol is not None:
            incomes = incomes.filter(symbol__iexact=symbol)

            income_serializer = IncomeSerializer(incomes, many=True)
            return JsonResponse(income_serializer.data, safe=False, )


@api_view(['GET'])
def symbol_income_detail(request, symbol, fyear):
    if request.method == 'GET':
        income = Income.objects.get(symbol=symbol, fiscal_year=fyear)

        income_serializer = IncomeSerializer(income)
        return JsonResponse(income_serializer.data)


@api_view(['GET'])
def income_init_annual(request):

    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        qincomes, vasymbol = data.get_income_statement_annual(symbol=symbol)

        for fical in qincomes['fiscalDateEnding']:
            income = qincomes[qincomes['fiscalDateEnding'] == fical]

            for col in income.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if income[col].values[0] == 'None':
                        income[col] = 0.0
                    else:
                        pass
                else:
                    pass

            inc = Income(
                symbol=symbol,
                report_type='quarterlyReport',
                fiscal_date_ending= datetime.strptime(income['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                fiscal_year=income['fiscalDateEnding'].values[0].split('-')[0],
                reported_currency=income['reportedCurrency'].values[0],
                total_revenue=income['totalRevenue'].values[0],
                total_operating_expense=income['totalOperatingExpense'].values[0],
                cost_of_revenue=income['costOfRevenue'].values[0],
                gross_profit=income['grossProfit'].values[0],
                ebit=income['ebit'].values[0],
                net_income=income['netIncome'].values[0],
                research_and_development=income['researchAndDevelopment'].values[0],
                effect_of_accounting_charges=income['effectOfAccountingCharges'].values[0],
                income_before_tax=income['incomeBeforeTax'].values[0],
                minority_interest=income['minorityInterest'].values[0],
                selling_general_administrative=income['sellingGeneralAdministrative'].values[0],
                other_non_operating_income=income['otherNonOperatingIncome'].values[0],
                operating_income=income['operatingIncome'].values[0],
                other_operating_expense=income['otherOperatingExpense'].values[0],
                interest_expense=income['interestExpense'].values[0],
                tax_provision=income['taxProvision'].values[0],
                interest_income=income['interestIncome'].values[0],
                net_interest_income=income['netInterestIncome'].values[0],
                extraordinary_items=income['extraordinaryItems'].values[0],
                non_recurring=income['nonRecurring'].values[0],
                other_items=income['otherItems'].values[0],
                income_tax_expense=income['incomeTaxExpense'].values[0],
                total_other_income_expense=income['totalOtherIncomeExpense'].values[0],
                discontinued_operations=income['discontinuedOperations'].values[0],
                net_income_from_continuing_operations=income['netIncomeFromContinuingOperations'].values[0],
                net_income_applicable_to_common_shares=income['netIncomeApplicableToCommonShares'].values[0],
                preferred_stock_and_other_adjustments=income['preferredStockAndOtherAdjustments'].values[0],
            )

            inc.save()

        return JsonResponse({'message': 'Annual Data Save successlly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def income_init_quarterly(request):

    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        qincomes, vasymbol = data.get_income_statement_quarterly(symbol=symbol)

        for fical in qincomes['fiscalDateEnding']:
            income = qincomes[qincomes['fiscalDateEnding'] == fical]

            for col in income.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if income[col].values[0] == 'None':
                        income[col] = 0.0
                    else:
                        pass
                else:
                    pass

            inc = Income(
                    symbol=symbol,
                    report_type='quarterlyReport',
                    fiscal_date_ending= datetime.strptime(income['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                    fiscal_year= income['fiscalDateEnding'].values[0].split('-')[0],
                    reported_currency=income['reportedCurrency'].values[0],
                    total_revenue=income['totalRevenue'].values[0],
                    total_operating_expense=income['totalOperatingExpense'].values[0],
                    cost_of_revenue=income['costOfRevenue'].values[0],
                    gross_profit=income['grossProfit'].values[0],
                    ebit=income['ebit'].values[0],
                    net_income=income['netIncome'].values[0],
                    research_and_development=income['researchAndDevelopment'].values[0],
                    effect_of_accounting_charges=income['effectOfAccountingCharges'].values[0],
                    income_before_tax=income['incomeBeforeTax'].values[0],
                    minority_interest=income['minorityInterest'].values[0],
                    selling_general_administrative=income['sellingGeneralAdministrative'].values[0],
                    other_non_operating_income=income['otherNonOperatingIncome'].values[0],
                    operating_income=income['operatingIncome'].values[0],
                    other_operating_expense=income['otherOperatingExpense'].values[0],
                    interest_expense=income['interestExpense'].values[0],
                    tax_provision=income['taxProvision'].values[0],
                    interest_income=income['interestIncome'].values[0],
                    net_interest_income=income['netInterestIncome'].values[0],
                    extraordinary_items=income['extraordinaryItems'].values[0],
                    non_recurring=income['nonRecurring'].values[0],
                    other_items=income['otherItems'].values[0],
                    income_tax_expense=income['incomeTaxExpense'].values[0],
                    total_other_income_expense=income['totalOtherIncomeExpense'].values[0],
                    discontinued_operations=income['discontinuedOperations'].values[0],
                    net_income_from_continuing_operations=income['netIncomeFromContinuingOperations'].values[0],
                    net_income_applicable_to_common_shares=income['netIncomeApplicableToCommonShares'].values[0],
                    preferred_stock_and_other_adjustments=income['preferredStockAndOtherAdjustments'].values[0],
            )

            inc.save()

        return JsonResponse({'message': 'Quarterly Data Save successlly'},  status=status.HTTP_200_OK)
