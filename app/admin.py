from django.contrib import admin

from .models import Currency, CurrencyComparison

admin.site.register(Currency)
admin.site.register(CurrencyComparison)
