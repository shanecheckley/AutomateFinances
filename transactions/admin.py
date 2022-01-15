from django.contrib import admin
from .models import Transaction, Envelope

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Envelope)