from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from cash_flows.models import CashFlow
from cash_flows.serializers import CashFlowSerializer
from rest_framework.decorators import api_view

from alpha_vantage.fundamentaldata import FundamentalData
from datetime import datetime


@api_view(['GET'])
def cashflow_list(request):
    if request.method == 'GET':
        cashflows = CashFlow.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            cashflows = cashflows.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        cashflow_serializer = CashFlowSerializer(cashflows, many=True)
        return JsonResponse(cashflow_serializer.data, safe=False, )

    elif request.method == 'DELETE':
        count = CashFlow.objects.all().delete()
        return JsonResponse({'message': '{} Companies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cashflow_detail(request, pk):
    try:
        cashflow = CashFlow.objects.get(pk=pk)

        if request.method == 'GET':
            cashflow_serializer = CashFlowSerializer(cashflow)
            return JsonResponse(cashflow_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def cashflow_init_annual(request):

    if request.method == 'GET':

        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        cashflows, vasymbol = data.get_cash_flow_annual(symbol=symbol)

        for fical in cashflows['fiscalDateEnding']:
            cashflow = cashflows[cashflows['fiscalDateEnding'] == fical]

            for col in cashflow.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if cashflow[col].values[0] == 'None':
                        cashflow[col] = 0.0
                    else:
                        pass
                else:
                    pass

            cash = CashFlow(
                symbol=symbol,
                report_type='annualReport',
                fiscal_date_ending= datetime.strptime(cashflow['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                reported_currency=cashflow['reportedCurrency'].values[0],
                investments=cashflow['investments'].values[0],
                change_in_liabilities=cashflow['changeInLiabilities'].values[0],
                cashflow_from_investment=cashflow['cashflowFromInvestment'].values[0],
                cashflow_from_financing=cashflow['cashflowFromFinancing'].values[0],
                other_cashflow_from_financing=cashflow['otherCashflowFromFinancing'].values[0],
                change_in_operating_activities=cashflow['changeInOperatingActivities'].values[0],
                net_income=cashflow['netIncome'].values[0],
                change_in_cash=cashflow['changeInCash'].values[0],
                operating_cashflow=cashflow['operatingCashflow'].values[0],
                other_operating_cashflow=cashflow['otherOperatingCashflow'].values[0],
                depreciation=cashflow['depreciation'].values[0],
                dividend_payout=cashflow['dividendPayout'].values[0],
                stock_sale_and_purchase=cashflow['stockSaleAndPurchase'].values[0],
                change_in_inventory=cashflow['changeInInventory'].values[0],
                change_in_account_receivables=cashflow['changeInAccountReceivables'].values[0],
                change_in_net_income=cashflow['changeInNetIncome'].values[0],
                capital_expenditures=cashflow['capitalExpenditures'].values[0],
                change_in_receivables=cashflow['changeInReceivables'].values[0],
                change_in_exchange_rate=cashflow['changeInExchangeRate'].values[0],
                change_in_cash_and_cash_equivalents=cashflow['changeInCashAndCashEquivalents'].values[0]
            )

            cash.save()

        return JsonResponse({'message': 'Annualy Data Save successlly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def cashflow_init_quarterly(request):

    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        data = FundamentalData(key='I7WB8M63PERU90OY', output_format='pandas')
        qcashflows, vasymbol = data.get_cash_flow_quarterly(symbol=symbol)

        for fical in qcashflows['fiscalDateEnding']:
            cashflow = qcashflows[qcashflows['fiscalDateEnding'] == fical]

            for col in cashflow.columns:
                if col not in ['fiscalDateEnding', 'reportedCurrency']:
                    if cashflow[col].values[0] == 'None':
                        cashflow[col] = 0.0
                    else:
                        pass
                else:
                    pass

            cash = CashFlow(
                symbol=symbol,
                report_type='annualReport',
                fiscal_date_ending= datetime.strptime(cashflow['fiscalDateEnding'].values[0], '%Y-%m-%d'),
                reported_currency=cashflow['reportedCurrency'].values[0],
                investments=cashflow['investments'].values[0],
                change_in_liabilities=cashflow['changeInLiabilities'].values[0],
                cashflow_from_investment=cashflow['cashflowFromInvestment'].values[0],
                other_cashflow_from_investment=cashflow['otherCashflowFromInvestment'].values[0],
                net_borrowings=cashflow['netBorrowings'].values[0],
                cashflow_from_financing=cashflow['cashflowFromFinancing'].values[0],
                other_cashflow_from_financing=cashflow['otherCashflowFromFinancing'].values[0],
                change_in_operating_activities=cashflow['changeInOperatingActivities'].values[0],
                net_income=cashflow['netIncome'].values[0],
                change_in_cash=cashflow['changeInCash'].values[0],
                operating_cashflow=cashflow['operatingCashflow'].values[0],
                other_operating_cashflow=cashflow['otherOperatingCashflow'].values[0],
                depreciation=cashflow['depreciation'].values[0],
                dividend_payout=cashflow['dividendPayout'].values[0],
                stock_sale_and_purchase=cashflow['stockSaleAndPurchase'].values[0],
                change_in_inventory=cashflow['changeInInventory'].values[0],
                change_in_account_receivables=cashflow['changeInAccountReceivables'].values[0],
                change_in_net_income=cashflow['changeInNetIncome'].values[0],
                capital_expenditures=cashflow['capitalExpenditures'].values[0],
                change_in_receivables=cashflow['changeInReceivables'].values[0],
                change_in_exchange_rate=cashflow['changeInExchangeRate'].values[0],
                change_in_cash_and_cash_equivalents=cashflow['changeInCashAndCashEquivalents'].values[0]
            )

            cash.save()

        return JsonResponse({'message': 'Quarterly Data Save successlly'},  status=status.HTTP_200_OK)
