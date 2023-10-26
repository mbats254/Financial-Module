from django.db import models
from Financialreportinganalytics.models import FinancialAccount, Transaction
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, blank=True, null=True)
    account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    
    def update_status(self):
        total_payments = self.payment_set.aggregate(models.Sum('amount_paid'))['amount_paid__sum']
        if total_payments >= self.total_amount:
            self.is_paid = True
        else:
            self.is_paid = False
        self.save()

    def __str__(self):
        return self.invoice_number

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

class CreditNote(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    
    def __str__(self):
        return self.customer

class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True) 
    order_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_received = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number

class PaymentReceipt(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    receipt_date = models.DateField()
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.id

class SupplierCreditNote(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    note_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    
    def __str__(self):
        return self.id
    
# Define the choices for report types
REPORT_TYPES = [
    ('financial_summary', 'Financial Summary'),
    ('invoice_summary', 'Invoice Summary'),
    ('payment_summary', 'Payment Summary'),
    # Add more report types as needed
]

# Define the choices for report formats
REPORT_FORMATS = [
    ('pdf', 'PDF'),
    ('csv', 'CSV'),
    ('xlsx', 'Excel'),
    # Add more report formats as needed
]

class Report(models.Model):
    report_name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    report_format = models.CharField(max_length=10, choices=REPORT_FORMATS)
    report_criteria = models.TextField()

    # Additional fields for associating with AccountReceivableAndPayable data
    transactions = models.ManyToManyField(Transaction, related_name='associated_reports')
    invoices = models.ManyToManyField('Invoice', related_name='associated_reports')
    payments = models.ManyToManyField('Payment', related_name='associated_reports')
    # Add more fields for other related data

    # Additional fields for filters or criteria specific to AccountReceivableAndPayable
    invoice_date_range = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    # Add more fields as needed       
    
# Define the PERMISSION_LEVELS as a list of choices
PERMISSION_LEVELS = [
    ('view', 'View'),
    ('edit', 'Edit'),
    ('delete', 'Delete'),
    # Add more permission levels as needed
]    
    
# Report Permissions
class ReportPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey('Report', on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=10, choices=PERMISSION_LEVELS)                   