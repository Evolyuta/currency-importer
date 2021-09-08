from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.urls import path

from services.currency_service import CurrencyService
from .models import CurrencyComparison, Currency


# Customizing CurrencyComparison model for admin panel
class CurrencyComparisonAdmin(admin.ModelAdmin):
    # Admin model table fields
    list_display = [
        'currency_title',
        'compared_currency_title',
        'ratio',
    ]

    # Setting custom changelist
    change_list_template = "currency_importer_changelist.html"

    # Custom routing
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_currencies),
        ]
        return my_urls + urls

    # Import request handler
    def import_currencies(self, request):
        currency_service = CurrencyService()

        import_errors = currency_service.import_currency_comparison_list()

        if import_errors:
            for import_error in import_errors:
                self.message_user(request, import_error, 30)

        return HttpResponseRedirect("../")


admin.site.register(Currency)
admin.site.register(CurrencyComparison, CurrencyComparisonAdmin)
