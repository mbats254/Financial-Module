from django.urls import path

from . import views
# Similar changes for JournalEntryList, JournalEntryDetail, FinancialTransactionList, and FinancialTransactionDetail
urlpatterns = [
    
    path('account/list', views.AccountList.as_view(), name='account-list'),
    path('account/detail/<int:pk>/', views.AccountDetail.as_view(), name='account-details'),
    path('journal/list', views.JournalEntryList.as_view(), name='journal-list'),
    path('journal/detail/<int:pk>/', views.JournalEntryDetail.as_view(), name='journal-details'),
    path('financial/list', views.FinancialTransactionList.as_view(), name='financial-list'),
    path('financial/detail/<int:pk>/', views.FinancialTransactionDetail.as_view(), name='financial-details'),

]