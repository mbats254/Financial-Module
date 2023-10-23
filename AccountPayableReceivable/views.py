from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.http import JsonResponse, Http404
from .models import Customer, Supplier, Invoice, Payment, CreditNote, PurchaseOrder, PaymentReceipt, SupplierCreditNote
from .serializers import (
    CustomerSerializer, SupplierSerializer,
    InvoiceSerializer, PaymentSerializer, CreditNoteSerializer,
    PurchaseOrderSerializer, PaymentReceiptSerializer, SupplierCreditNoteSerializer
)
from django.conf import settings

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
        # return Response('dsfsdfsd:'+self)
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
                              
            
            
            # return Response('dsfsdfsd:'+self.serializer, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def send_registration_email(email):
        subject = 'Registration Confirmation'
        message = 'Welcome. Thank you for registering with us.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)    

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
            raise Http404

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
    def post(self, request, format=None):
        # return Response('dsfsdfsd:'+self)
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Check the model type and send a registration email if it's a Customer
            
            send_registration_email(serializer.data['email'])
          
            # return Response('dsfsdfsd:'+self.serializer, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        
    def post(self, request, format=None):
        try:
            invoice = Invoice.objects.get(pk=request.data['invoice'])
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        payment_amount = request.data.get('amount_paid')

        # Check if the payment amount is equal to or greater than the invoice amount
        if payment_amount >= invoice.total_amount:
            # Create a payment record
            payment = Payment.objects.create(invoice=invoice, payment_date=invoice.due_date, amount_paid=payment_amount)

            # Call the update_status method to update the invoice status
            invoice.update_status()

            # Determine if the supplier or customer should receive the notification
            recipient_email =  invoice.customer.email
            recipient_name = invoice.customer.name

            # Send a notification email to the recipient
            subject = 'Payment Received'
            message = f'Thank you for the payment of Ksh.{payment_amount} for Invoice #{invoice.invoice_number}.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [recipient_email]

            send_mail(subject, message, from_email, recipient_list)

            return Response({'message': 'Invoice marked as paid, and a notification has been sent.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Payment amount is insufficient.'}, status=status.HTTP_400_BAD_REQUEST)

class PaymentDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Payment, PaymentSerializer)

class CreditNoteList(BaseAPIListView):
    def __init__(self):
        super().__init__(CreditNote, CreditNoteSerializer)
    def post(self, request, format=None):
        scenario = request.query_params.get('scenario', 'standard')
        customer = Customer.objects.get(id=request.data['customer'])
        customerSerializer = CustomerSerializer(customer, many=False)
        # return Response(customerSerializer.data)
        if scenario == 'standard':
            # Handle a standard credit note creation
            # Create and save the credit note
            # You may need to provide details such as the customer, amount, reason, etc.
            credit_note = CreditNote.objects.create(customer=customer, amount=request.data['amount'], reason=request.data['reason'], note_date=request.data['note_date'])

        elif scenario == 'discount':
            # Handle a discount credit note creation
            # Create and save the credit note
            # You may need to specify the invoice to apply the discount to
            credit_note = CreditNote.objects.create(customer=customer, amount=-request.data['discount_amount'], reason='Discount on Invoice', note_date=request.data['note_date'])

        elif scenario == 'cancellation':
            # Handle a credit note for canceling an invoice
            # Create and save the credit note
            # You may need to specify the invoice being canceled
            credit_note = CreditNote.objects.create(customer=customer, amount=-request.data['cancellation_amount'], reason='Cancellation of Invoice', note_date=request.data['note_date'])

        elif scenario == 'prepayment':
            # Handle a credit note for a prepayment
            # Create and save the credit note
            # You may need to specify the prepayment amount
            credit_note = CreditNote.objects.create(customer=customer, amount=request.data['prepayment_amount'], reason='Prepayment', note_date=request.data['note_date'])

        else:
            return Response({'message': 'Invalid scenario.'}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the credit note
        serializer = CreditNoteSerializer(credit_note)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    

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

# # Helper function to send registration emails
def send_registration_email(email):
    subject = 'Registration Confirmation'
    message = 'Thank you for registering.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

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
