from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)  # E.g., Asset, Liability, Equity, Revenue, Expense

    def __str__(self):
        return self.name
    
class JournalEntryLine(models.Model):
    journal_entry = models.ForeignKey('JournalEntry', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class FinancialTransaction(models.Model):
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction on {self.date}: {self.description}"
    