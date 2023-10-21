from django.urls import path

from . import views

urlpatterns = [
    # path("apioverview", views.ApiOverview, name="api_overview"),  
    path('income/list', views.IncomeList.as_view(), name='income-list'),
    path('income/detail/<int:pk>', views.IncomeDetail.as_view(), name='income-detail'),
    path('expense/list', views.ExpenseList.as_view(), name='expense-list'),
    path('expense/detail/<int:pk>', views.ExpenseDetail.as_view(), name='expense-detail'),
    path('financial/list', views.FinancialHealthList.as_view(), name='financial-list'),
    path('financial/detail/<int:pk>', views.FinancialHealthDetail.as_view(), name='financial-detail'),
    path('income/list', views.IncomeList.as_view(), name='income-list'),
    path('income/detail/<int:pk>', views.IncomeDetail.as_view(), name='income-detail'),
    path('income/view/set', views.IncomeViewSet.as_view(), name='income-view-set'),
    path('expense/view/set', views.ExpenseViewSet.as_view(), name='expense-view-set'),
    path('financial/health/view/set', views.FinancialHealthViewSet.as_view(), name='expense-view-set'),
]