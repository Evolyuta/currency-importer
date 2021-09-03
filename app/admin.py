from django.contrib import admin

from .models import CurrencyComparison


# Customizing CurrencyComparison model for admin panel
class CurrencyComparisonAdmin(admin.ModelAdmin):
    # Admin model table fields
    list_display = [
        'currency_title',
        'compared_currency_title',
        'ratio',
    ]


admin.site.register(CurrencyComparison, CurrencyComparisonAdmin)
