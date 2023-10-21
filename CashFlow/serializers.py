from rest_framework import serializers
from .models import Income, Expense, FinancialHealth, BankReconciliation, CashForecast, BankTransaction

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class FinancialHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialHealth
        fields = '__all__'

class BankReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankReconciliation
        fields = '__all__'

class CashForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashForecast
        fields = '__all__'

class BankTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransaction
        fields = '__all__'