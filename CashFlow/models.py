from django.db import models

# Create your models here.
class Income(models.Model):
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Income from {self.source} on {self.date}"
    
class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Expense in {self.category} on {self.date}"
         
class FinancialHealth(models.Model):
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    assets = models.DecimalField(max_digits=10, decimal_places=2)
    liabilities = models.DecimalField(max_digits=10, decimal_places=2)
    net_worth = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Financial Health (Net Worth: {self.net_worth})"
    
class BankReconciliation(models.Model):
    date = models.DateField()
    bank_account = models.ForeignKey('BankAccount', on_delete=models.CASCADE)
    statement_balance = models.DecimalField(max_digits=10, decimal_places=2)
    actual_balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_reconciled = models.BooleanField(default=False)

    def __str__(self):
        return f"Bank Reconciliation for {self.bank_account} on {self.date}"
    
    
class CashForecast(models.Model):
    date = models.DateField()
    cash_account = models.ForeignKey('CashAccount', on_delete=models.CASCADE)
    forecasted_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cash Forecast for {self.cash_account} on {self.date}"


class BankTransaction(models.Model):
    date = models.DateField()
    bank_account = models.ForeignKey('BankAccount', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} in {self.bank_account} on {self.date}"            