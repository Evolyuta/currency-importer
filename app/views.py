from django.shortcuts import render

from services.currency_service import CurrencyService


def currency_importer_view(request):
    if request.method == 'POST':
        currency_service = CurrencyService()

        currency_service.import_currency_list()
        currency_service.import_currency_compare_list()

    return render(request, 'currency-importer.html', {})
