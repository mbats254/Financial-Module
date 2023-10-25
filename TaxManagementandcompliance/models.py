from django.db import models
from AccountPayableReceivable.models import Customer, Supplier, Invoice

class TaxRate(models.Model):
    rate_name = models.CharField(max_length=50)
    rate_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

class TaxType(models.Model):
    type_name = models.CharField(max_length=50)
    description = models.TextField()

class TaxExemption(models.Model):
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    tax_type = models.ForeignKey(TaxType, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

class TaxDeduction(models.Model):
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    tax_type = models.ForeignKey(TaxType, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)
    deduction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class TaxPayment(models.Model):
    payment_date = models.DateField()
    tax_type = models.ForeignKey(TaxType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

class TaxReturn(models.Model):
    return_type = models.CharField(max_length=50)
    return_period = models.CharField(max_length=50)
    submitted_date = models.DateField()
    status = models.CharField(max_length=50)

class TaxAuthority(models.Model):
    authority_name = models.CharField(max_length=50)
    jurisdiction = models.CharField(max_length=50)
    contact_info = models.TextField()

class TaxComplianceDocument(models.Model):
    document_type = models.CharField(max_length=50)
    document_number = models.CharField(max_length=20)
    document_date = models.DateField()
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    tax_type = models.ForeignKey(TaxType, on_delete=models.CASCADE)
    description = models.TextField()

class TaxJurisdiction(models.Model):
    jurisdiction_name = models.CharField(max_length=50)
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE)
    tax_authority = models.ForeignKey(TaxAuthority, on_delete=models.CASCADE)

class TaxConfiguration(models.Model):
    configuration_name = models.CharField(max_length=50)
    tax_type = models.ForeignKey(TaxType, on_delete=models.CASCADE)
    rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_to = models.DateField(null=True, blank=True)

class Entity(models.Model):
    entity_name = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=50)


# Add more fields and relationships as needed for your specific requirements.
