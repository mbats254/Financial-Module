from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
 # Create your views here.



class BaseAPIListView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        items = self.model.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BaseAPIDetailView(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get(self, request, pk):
        instance = self.get_object(pk)
        if instance is not None:
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        instance = self.get_object(pk)
        if instance is not None:
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        if instance is not None:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class TaxRateListView(BaseAPIListView):
    model = TaxRate
    serializer_class = TaxRateSerializer

class TaxRateDetailView(BaseAPIDetailView):
    model = TaxRate
    serializer_class = TaxRateSerializer

class TaxTypeListView(BaseAPIListView):
    model = TaxType
    serializer_class = TaxTypeSerializer

class TaxTypeDetailView(BaseAPIDetailView):
    model = TaxType
    serializer_class = TaxTypeSerializer    
    

class TaxExemptionDetailView(BaseAPIDetailView):
    model = TaxExemption
    serializer_class = TaxExemptionSerializer    

class TaxDeductionListView(BaseAPIListView):
    model = TaxDeduction
    serializer_class = TaxDeductionSerializer

class TaxDeductionDetailView(BaseAPIDetailView):
    model = TaxDeduction
    serializer_class = TaxDeductionSerializer    

class TaxPaymentListView(BaseAPIListView):
    model = TaxPayment
    serializer_class = TaxPaymentSerializer

class TaxPaymentDetailView(BaseAPIDetailView):
    model = TaxPayment
    serializer_class = TaxPaymentSerializer    

class TaxReturnListView(BaseAPIListView):
    model = TaxReturn
    serializer_class = TaxReturnSerializer

class TaxReturnDetailView(BaseAPIDetailView):
    model = TaxReturn
    serializer_class = TaxReturnSerializer    

class TaxAuthorityListView(BaseAPIListView):
    model = TaxAuthority
    serializer_class = TaxAuthoritySerializer

class TaxAuthorityDetailView(BaseAPIDetailView):
    model = TaxAuthority
    serializer_class = TaxAuthoritySerializer    

class TaxComplianceDocumentListView(BaseAPIListView):
    model = TaxComplianceDocument
    serializer_class = TaxComplianceDocumentSerializer

class TaxComplianceDocumentDetailView(BaseAPIDetailView):
    model = TaxComplianceDocument
    serializer_class = TaxComplianceDocumentSerializer    

class TaxJurisdictionListView(BaseAPIListView):
    model = TaxJurisdiction
    serializer_class = TaxJurisdictionSerializer

class TaxJurisdictionDetailView(BaseAPIDetailView):
    model = TaxJurisdiction
    serializer_class = TaxJurisdictionSerializer    

class TaxConfigurationListView(BaseAPIListView):
    model = TaxConfiguration
    serializer_class = TaxConfigurationSerializer

class TaxConfigurationDetailView(BaseAPIDetailView):
    model = TaxConfiguration
    serializer_class = TaxConfigurationSerializer    

class EntityListView(BaseAPIListView):
    model = Entity
    serializer_class = EntitySerializer

class EntityDetailView(BaseAPIDetailView):
    model = Entity
    serializer_class = EntitySerializer    
