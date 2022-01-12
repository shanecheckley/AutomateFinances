from django.db import models

# Create your models here.

class transaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    transaction_type = models.CharField(max_length=9)
    amount = models.DecimalField(decimal_places=2,max_digits=9)
    debit_or_credit = models.CharField(max_length=6)
    purchase_method = models.CharField(max_length=15)