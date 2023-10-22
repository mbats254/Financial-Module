from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, JournalEntry, FinancialTransaction
from .serializers import AccountSerializer, JournalEntrySerializer, FinancialTransactionSerializer

class AccountList(APIView):
    """
    List all accounts or create a new account.
    """
    def get(self, request, format=None):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    """
    Retrieve, update, or delete an account.
    """
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        if account is not None:
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        if account is not None:
            serializer = AccountSerializer(account, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        if account is not None:
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)




class JournalEntryList(APIView):
    """
    List all journal entries or create a new journal entry.
    """
    def get(self, request, format=None):
        entries = JournalEntry.objects.all()
        serializer = JournalEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JournalEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalEntryDetail(APIView):
    """
    Retrieve, update, or delete a journal entry.
    """
    def get_object(self, pk):
        try:
            return JournalEntry.objects.get(pk=pk)
        except JournalEntry.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        entry = self.get_object(pk)
        if entry is not None:
            serializer = JournalEntrySerializer(entry)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        entry = self.get_object(pk)
        if entry is not None:
            serializer = JournalEntrySerializer(entry, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        entry = self.get_object(pk)
        if entry is not None:
            entry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class FinancialTransactionList(APIView):
    """
    List all financial transactions or create a new financial transaction.
    """
    def get(self, request, format=None):
        transactions = FinancialTransaction.objects.all()
        serializer = FinancialTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FinancialTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FinancialTransactionDetail(APIView):
    """
    Retrieve, update, or delete a financial transaction.
    """
    def get_object(self, pk):
        try:
            return FinancialTransaction.objects.get(pk=pk)
        except FinancialTransaction.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        transaction = self.get_object(pk)
        if transaction is not None:
            serializer = FinancialTransactionSerializer(transaction)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        transaction = self.get_object(pk)
        if transaction is not None:
            serializer = FinancialTransactionSerializer(transaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        transaction = self.get_object(pk)
        if transaction is not None:
            transaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
