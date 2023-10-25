from rest_framework import serializers
from .models import *


class TaxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRate
        fields = '__all__'

class TaxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxType
        fields = '__all__'

class TaxExemptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxExemption
        fields = '__all__'

class TaxDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeduction
        fields = '__all__'

class TaxPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxPayment
        fields = '__all__'

class TaxReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxReturn
        fields = '__all__'

class TaxAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxAuthority
        fields = '__all__'

class TaxComplianceDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxComplianceDocument
        fields = '__all__'

class TaxJurisdictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxJurisdiction
        fields = '__all__'

class TaxConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxConfiguration
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'