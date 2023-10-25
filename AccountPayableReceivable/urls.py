from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for Customer model
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),

    # URL patterns for Supplier model
    path('suppliers/', views.SupplierList.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', views.SupplierDetail.as_view(), name='supplier-detail'),

    # URL patterns for Invoice model
    path('invoices/', views.InvoiceList.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice-detail'),

    # URL patterns for Payment model
    path('payments/list', views.PaymentList.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetail.as_view(), name='payment-detail'),

    # URL patterns for CreditNote model
    path('creditnotes/', views.CreditNoteList.as_view(), name='creditnote-list'),
    path('creditnotes/<int:pk>/', views.CreditNoteDetail.as_view(), name='creditnote-detail'),

    # URL patterns for PurchaseOrder model
    path('purchaseorders/', views.PurchaseOrderList.as_view(), name='purchaseorder-list'),
    path('purchaseorders/<int:pk>/', views.PurchaseOrderDetail.as_view(), name='purchaseorder-detail'),

    # URL patterns for PaymentReceipt model
    path('paymentreceipts/', views.PaymentReceiptList.as_view(), name='paymentreceipt-list'),
    path('paymentreceipts/<int:pk>/', views.PaymentReceiptDetail.as_view(), name='paymentreceipt-detail'),

    # URL patterns for SupplierCreditNote model
    path('suppliercreditnotes/', views.SupplierCreditNoteList.as_view(), name='suppliercreditnote-list'),
    path('suppliercreditnotes/<int:pk>/', views.SupplierCreditNoteDetail.as_view(), name='suppliercreditnote-detail'),

    # Custom actions
    path('invoices/mark_paid/', views.InvoicePayment.as_view(), name='mark-invoice-paid'),
]
    