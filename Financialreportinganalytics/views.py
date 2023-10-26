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

class FinancialStatementGenerator:
    @staticmethod
    def generate_income_statement():
        # Get all income and expense accounts
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

        return {
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'net_income': net_income,
        }

    @staticmethod
    def generate_balance_sheet():
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

        return {
            'total_assets': total_assets,
            'total_liabilities': total_liabilities,
            'owner_equity': owner_equity,
        }
 
        
        
class VarianceAnalysis:
    @staticmethod
    def calculate_variance(budget_category_id):
        # Get the budget category
        budget_category = BudgetCategory.objects.get(pk=budget_category_id)

        # Get the actual total for the budget category
        actual_total = FinancialStatement.objects.filter(
            account__budget_category=budget_category,
        ).aggregate(total=models.Sum('amount'))['total'] or 0

        # Get the budgeted total for the budget category
        budget_total = Budget.objects.filter(
            budget_category=budget_category,
        ).aggregate(total=models.Sum('amount'))['total'] or 0

        # Calculate the variance
        variance = actual_total - budget_total

        return {
            'budget_category': budget_category,
            'actual_total': actual_total,
            'budget_total': budget_total,
            'variance': variance,
        }        
    
    
 