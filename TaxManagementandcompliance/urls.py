from django.urls import path

from . import views

urlpatterns = [
    # path("apioverview", views.ApiOverview, name="api_overview"),  
    path('rate/list', views.TaxRateListView.as_view(), name='tax-rate-list'),
    path('rate/detail/<int:pk>/', views.TaxRateDetailView.as_view(), name='tax-rate-detail'),
    path('type/list', views.TaxTypeListView.as_view(), name='tax-type-list'),
    path('type/detail/<int:pk>/', views.TaxTypeDetailView.as_view(), name='tax-type-detail'),
   
   
    # path('expense/view/set', views.ExpenseViewSet.as_view(), name='expense-view-set'),
    # path('financial/health/view/set', views.FinancialHealthViewSet.as_view(), name='expense-view-set'),
]