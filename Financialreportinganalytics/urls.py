from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for Customer model
    path('account/', views.FinancialAccountList.as_view(), name='account-list'),
    path('account/<int:pk>/', views.FinancialAccountDetail.as_view(), name='account-detail'),
    path('budget/category/', views.BudgetCategoryList.as_view(), name='budget-category-list'),
    path('budget/category/<int:pk>/', views.BudgetCategoryDetail.as_view(), name='budget-category-detail'),
    path('budget/', views.BudgetList.as_view(), name='budget-list'),
    path('budget/<int:pk>/', views.BudgetDetail.as_view(), name='budget-detail'),
     # URL pattern for generating an income statement
    path('generate_income_statement/', views.FinancialStatementGenerator.as_view(), name='generate_income_statement'),
    # URL pattern for generating a balance sheet    
    path('generate_balance_sheet/', views.GenerateBalanceSheet.as_view(), name='generate_balance_sheet'),
    # URL pattern for calculate variance    
    path('calculate/variance/', views.VarianceAnalysis.as_view(), name='variance-calculate'),
    
    
]