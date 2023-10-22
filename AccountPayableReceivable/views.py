from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Supplier, Invoice, Payment, CreditNote, PurchaseOrder, PaymentReceipt, SupplierCreditNote
from .serializers import (
    CustomerSerializer, SupplierSerializer,
    InvoiceSerializer, PaymentSerializer, CreditNoteSerializer,
    PurchaseOrderSerializer, PaymentReceiptSerializer, SupplierCreditNoteSerializer
)

class BaseAPIListView(APIView):
    """
    Base class for list/create operations.
    """
    def __init__(self, model, serializer):
        self.model = model
        self.serializer = serializer

    def get(self, request, format=None):
        items = self.model.objects.all()
        serializer = self.serializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BaseAPIDetailView(APIView):
    """
    Base class for retrieve/update/delete operations.
    """
    def __init__(self, model, serializer):
        self.model = model
        self.serializer = serializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        if item is not None:
            serializer = self.serializer(item)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        if item is not None:
            serializer = self.serializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        if item is not None:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class CustomerList(BaseAPIListView):
    def __init__(self):
        super().__init__(Customer, CustomerSerializer)

class CustomerDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Customer, CustomerSerializer)
        
class CustomerList(BaseAPIListView):
    def __init__(self):
        super().__init__(Customer, CustomerSerializer)

class CustomerDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Customer, CustomerSerializer)

class SupplierList(BaseAPIListView):
    def __init__(self):
        super().__init__(Supplier, SupplierSerializer)

class SupplierDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Supplier, SupplierSerializer)

class InvoiceList(BaseAPIListView):
    def __init__(self):
        super().__init__(Invoice, InvoiceSerializer)

class InvoiceDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Invoice, InvoiceSerializer)

class PaymentList(BaseAPIListView):
    def __init__(self):
        super().__init__(Payment, PaymentSerializer)

class PaymentDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Payment, PaymentSerializer)

class CreditNoteList(BaseAPIListView):
    def __init__(self):
        super().__init__(CreditNote, CreditNoteSerializer)

class CreditNoteDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(CreditNote, CreditNoteSerializer)

class PurchaseOrderList(BaseAPIListView):
    def __init__(self):
        super().__init__(PurchaseOrder, PurchaseOrderSerializer)

class PurchaseOrderDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(PurchaseOrder, PurchaseOrderSerializer)

class PaymentReceiptList(BaseAPIListView):
    def __init__(self):
        super().__init__(PaymentReceipt, PaymentReceiptSerializer)

class PaymentReceiptDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(PaymentReceipt, PaymentReceiptSerializer)

class SupplierCreditNoteList(BaseAPIListView):
    def __init__(self):
        super().__init__(SupplierCreditNote, SupplierCreditNoteSerializer)

class SupplierCreditNoteDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(SupplierCreditNote, SupplierCreditNoteSerializer)        

# 

class InvoicePayment(APIView):
    """
    Mark an invoice as paid.
    """
    def post(self, request, invoice_id, format=None):
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Update the invoice's is_paid status
        invoice.is_paid = True
        invoice.save()

        # Create a payment record
        Payment.objects.create(invoice=invoice, payment_date=invoice.due_date, amount_paid=invoice.total_amount)

        return Response({'message': 'Invoice marked as paid.'}, status=status.HTTP_200_OK)

# Add more APIView classes and functions as needed for custom actions and interactions between the models
