# Generated by Django 4.0.1 on 2022-01-31 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_transaction_income_transaction_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='trans_id',
        ),
    ]
