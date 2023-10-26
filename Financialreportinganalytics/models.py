from django.db import models

# Create your models here.
# Define the ACCOUNT_TYPES as a list of choices
ACCOUNT_TYPES = [
    ('asset', 'Asset'),
    ('liability', 'Liability'),
    ('income', 'Income'),
    ('expense', 'Expense'),
]

# Define the STATEMENT_TYPES as a list of choices
STATEMENT_TYPES = [
    ('income_statement', 'Income Statement (Profit and Loss)'),
    ('balance_sheet', 'Balance Sheet'),
    # Add more statement types as needed
]


# Financial Accounts
class FinancialAccount(models.Model):
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    description = models.TextField()
    
# Transactions
class Transaction(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    source_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, related_name='source_transactions')
    target_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, related_name='target_transactions')
    
# Budgeting
class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField()

class Budget(models.Model):
    budget_period = models.DateField()
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
# Financial Statements
class FinancialStatement(models.Model):
    statement_type = models.CharField(max_length=20, choices=STATEMENT_TYPES)
    date = models.DateField()
    account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class FinancialStatementCategory(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField()
    
    
# Variance Analysis
class VarianceAnalysis(models.Model):
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2)
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    variance = models.DecimalField(max_digits=10, decimal_places=2) 
    
# Chart of Accounts
class ChartOfAccounts(models.Model):
    account_code = models.CharField(max_length=10)
    account_name = models.CharField(max_length=255)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
 
    
