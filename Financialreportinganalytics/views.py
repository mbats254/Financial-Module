from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.http import JsonResponse, Http404
from .models import *
from .serializers import *
# Create your views here.
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
 
 
class FinancialAccountList(BaseAPIListView):
    def __init__(self):
        super().__init__(FinancialAccount, FinancialAccountSerializer)

class FinancialAccountDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(FinancialAccount, FinancialAccountSerializer)
 
class BudgetCategoryList(BaseAPIListView):
    def __init__(self):
        super().__init__(BudgetCategory, BudgetCategorySerializer)

class BudgetCategoryDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(BudgetCategory, BudgetCategorySerializer)
 
class BudgetList(BaseAPIListView):
    def __init__(self):
        super().__init__(Budget, BudgetSerializer)

class BudgetDetail(BaseAPIDetailView):
    def __init__(self):
        super().__init__(Budget, BudgetSerializer)
 
from .models import FinancialStatement, FinancialAccount

class FinancialStatementGenerator(APIView):   
    def get(self, request, format=None):
        income_accounts = FinancialAccount.objects.filter(account_type='income')
        expense_accounts = FinancialAccount.objects.filter(account_type='expense')

        # Calculate total revenue (income)
        total_revenue = sum(
            FinancialStatement.objects.filter(account__in=income_accounts)
            .values_list('amount', flat=True)
        )

        # Calculate total expenses
        total_expenses = sum(
            FinancialStatement.objects.filter(account__in=expense_accounts)
            .values_list('amount', flat=True)
        )

        # Calculate net income (revenue - expenses)
        net_income = total_revenue - total_expenses

        response =  {
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'net_income': net_income,
        }
        
        return Response(response)
        # return Response(status=status.HTTP_404_NOT_FOUND)

    
        
    

class GenerateBalanceSheet(APIView):  
    def get(self ,request, format=None):
        # Get all asset and liability accounts
        asset_accounts = FinancialAccount.objects.filter(account_type='asset')
        liability_accounts = FinancialAccount.objects.filter(account_type='liability')

        # Calculate total assets
        total_assets = sum(
            FinancialStatement.objects.filter(account__in=asset_accounts)
            .values_list('amount', flat=True)
        )

        # Calculate total liabilities
        total_liabilities = sum(
            FinancialStatement.objects.filter(account__in=liability_accounts)
            .values_list('amount', flat=True)
        )

        # Calculate owner's equity (assets - liabilities)
        owner_equity = total_assets - total_liabilities

        return Response( {
            'total_assets': total_assets,
            'total_liabilities': total_liabilities,
            'owner_equity': owner_equity,
        })
 

        
class VarianceAnalysis(APIView):
    def post(self ,request, format=None):
        # Get the budget category
        budget_category = BudgetCategory.objects.get(pk=request.data['budget_category_id'])

        # Get the financial accounts associated with the budget category
        financial_accounts = FinancialAccount.objects.filter(account_type=budget_category.category_name.split('_')[0])

        # Calculate the actual total spent for the financial accounts
        actual_total_spent = FinancialStatement.objects.filter(
            account__in=financial_accounts,
        ).aggregate(total=models.Sum('amount'))['total'] or 0

        # Get the total budget for the budget category
        total_budget = Budget.objects.filter(
            category=budget_category,
        ).aggregate(total=models.Sum('amount'))['total'] or 0

        # Calculate the variance (actual total spent - total budget)
        variance = actual_total_spent - total_budget

        return Response( {
            'budget_category': budget_category,
            'actual_total': actual_total_spent,
            'budget_total': total_budget,
            'variance': variance,
        })      
    
    
 