from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

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

class SupplierCreditNote(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    note_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()