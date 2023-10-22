from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Supplier, Invoice, Payment, CreditNote, PurchaseOrder, PaymentReceipt, SupplierCreditNote

class AccountsPayableTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_customer_api(self):
        # Create a Customer
        response = self.client.post("/account/payable/customers/", {"name": "Test Customer"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the Customer
        response = self.client.get(f"/account/payable/customers/{response.data['id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Customer")

        # Update the Customer
        response = self.client.put(f"/account/payable/customers/{response.data['id']}/", {"name": "Updated Customer"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Customer")

        # Delete the Customer
        response = self.client.delete(f"/account/payable/customers/{response.data['id']}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Add similar tests for Supplier, Invoice, Payment, CreditNote, PurchaseOrder, PaymentReceipt, and SupplierCreditNote models

    def test_invoice_payment(self):
        # Create an Invoice
        response = self.client.post("/account/payable/invoices/", {"total_amount": 100})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        invoice_id = response.data['id']

        # Mark the Invoice as paid
        response = self.client.post(f"/account/payable/invoices/{invoice_id}/mark_paid/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the Invoice is marked as paid
        response = self.client.get(f"/account/payable/invoices/{invoice_id}/")
        self.assertTrue(response.data["is_paid"])

        # Clean up: Delete the Invoice
        response = self.client.delete(f"/account/payable/invoices/{invoice_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
