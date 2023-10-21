from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Income, Expense, FinancialHealth
from .serializers import IncomeSerializer, ExpenseSerializer, FinancialHealthSerializer
from datetime import date, timedelta
from rest_framework.views import APIView

class IncomeList(APIView):
    """
    List all income records or create a new income record.
    """
    def get(self, request, format=None):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeDetail(APIView):
    """
    Retrieve, update, or delete an income record.
    """
    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        income = self.get_object(pk)
        if income is not None:
            serializer = IncomeSerializer(income)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        income = self.get_object(pk)
        if income is not None:
            serializer = IncomeSerializer(income, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        income = self.get_object(pk)
        if income is not None:
            income.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

class ExpenseList(APIView):
    """
    List all expense records or create a new expense record.
    """
    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseDetail(APIView):
    """
    Retrieve, update, or delete an expense record.
    """
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        expense = self.get_object(pk)
        if expense is not None:
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk)
        if expense is not None:
            serializer = ExpenseSerializer(expense, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        if expense is not None:
            expense.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)    

class FinancialHealthList(APIView):
    """
    List all financial health records or create a new financial health record.
    """
    def get(self, request, format=None):
        financial_health = FinancialHealth.objects.all()
        serializer = FinancialHealthSerializer(financial_health, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FinancialHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FinancialHealthDetail(APIView):
    """
    Retrieve, update, or delete a financial health record.
    """
    def get_object(self, pk):
        try:
            return FinancialHealth.objects.get(pk=pk)
        except FinancialHealth.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        financial_health = self.get_object(pk)
        if financial_health is not None:
            serializer = FinancialHealthSerializer(financial_health)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        financial_health = self.get_object(pk)
        if financial_health is not None:
            serializer = FinancialHealthSerializer(financial_health, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        financial_health = self.get_object(pk)
        if financial_health is not None:
            financial_health.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def income_summary(self, request):
        # Calculate and return summary data, e.g., total income for a given period.
        # You can customize this action as needed.
        thirty_days_ago = date.today() - timedelta(days=30)
        total_income = Income.objects.filter(date__gte=thirty_days_ago).aggregate(total=Sum('amount'))['total']

        return Response({'total_income': total_income})

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def expense_summary(self, request):
        # Calculate and return summary data, e.g., total expenses for a given period.
        # You can customize this action as needed.
        thirty_days_ago = date.today() - timedelta(days=30)
        total_expenses = Expense.objects.filter(date__gte=thirty_days_ago).aggregate(total=Sum('amount'))['total']

        return Response({'total_expenses': total_expenses})

class FinancialHealthViewSet(viewsets.ModelViewSet):
    queryset = FinancialHealth.objects.all()
    serializer_class = FinancialHealthSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Set the organization field when creating a new financial health record.
        serializer.save(organization=self.request.user.organization)  # Replace with your authentication and organization setup.

    @action(detail=False, methods=['get'])
    def organization_summary(self, request):
        # Calculate and return summary data for the organization's financial health.
        # You can customize this action as needed.
        organization = request.user.organization

        # Calculate the organization's financial health indicators
        financial_health = FinancialHealth.objects.filter(organization=organization).latest('date')

        return Response({
            'cash_balance': financial_health.cash_balance,
            'assets': financial_health.assets,
            'liabilities': financial_health.liabilities,
            'net_worth': financial_health.net_worth,
        })
