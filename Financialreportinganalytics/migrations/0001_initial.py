# Generated by Django 4.2.4 on 2023-10-25 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('asset', 'Asset'), ('liability', 'Liability'), ('income', 'Income'), ('expense', 'Expense')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatementCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VarianceAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budgeted_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('variance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financialreportinganalytics.budgetcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('source_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_transactions', to='Financialreportinganalytics.financialaccount')),
                ('target_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_transactions', to='Financialreportinganalytics.financialaccount')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement_type', models.CharField(choices=[('income_statement', 'Income Statement (Profit and Loss)'), ('balance_sheet', 'Balance Sheet')], max_length=20)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financialreportinganalytics.financialaccount')),
            ],
        ),
        migrations.CreateModel(
            name='ChartOfAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_code', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('asset', 'Asset'), ('liability', 'Liability'), ('income', 'Income'), ('expense', 'Expense')], max_length=20)),
                ('parent_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Financialreportinganalytics.chartofaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_period', models.DateField()),
                ('allocated_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Financialreportinganalytics.budgetcategory')),
            ],
        ),
    ]
