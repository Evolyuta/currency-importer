from django.contrib import admin

from .models import Currency, CurrencyCompare

admin.site.register(Currency)
admin.site.register(CurrencyCompare)
