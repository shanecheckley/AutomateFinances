from django.db import models
from django.db.models.base import Model

# Create your models here.

class Envelope(models.Model):
    name = models.CharField(max_length=25)
    balance = models.DecimalField(decimal_places=2,max_digits=9)

    def __str__(self):
        return self.name + ' | ' + self.balance

class Transaction(models.Model):
    envelope = models.ForeignKey(Envelope, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    transaction_type = models.CharField(max_length=9)
    amount = models.DecimalField(decimal_places=2,max_digits=9)
    debit_or_credit = models.CharField(max_length=6)
    purchase_method = models.CharField(max_length=15)

    def __str__(self):
        return self.date + ' | ' + self.description + ' | ' + self.amount