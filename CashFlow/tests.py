from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer

# Create your tests here.
class FinanceModuleTests(TestCase):
    def setUp(self):
        # Create test data for Income and Expense
        self.income_data = {'source': 'Test Source', 'amount': 100.00}
        self.income = Income.objects.create(**self.income_data)

        self.expense_data = {'description': 'Test Expense', 'amount': 50.00}
        self.expense = Expense.objects.create(**self.expense_data)

    def test_list_incomes(self):
        url = reverse('income-list')
        response = self.client.get(url)
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_income(self):
        url = reverse('income-list')
        response = self.client.post(url, self.income_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Income.objects.count(), 2)

    def test_retrieve_income(self):
        url = reverse('income-detail', args=[self.income.id])
        response = self.client.get(url)
        serializer = IncomeSerializer(self.income)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_income(self):
        url = reverse('income-detail', args=[self.income.id])
        updated_data = {'source': 'Updated Source', 'amount': 150.00}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.income.refresh_from_db()
        self.assertEqual(self.income.source, updated_data['source'])

    def test_delete_income(self):
        url = reverse('income-detail', args=[self.income.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Income.objects.count(), 0)

    # Similar tests for ExpenseList and ExpenseDetail

