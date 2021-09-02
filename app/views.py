from django.shortcuts import render

from services.currency_api_service import CurrencyApiService
from services.currency_service import CurrencyService


def currency_importer_view(request, *args, **kwargs):
    if request.method == 'POST':
        api_service = CurrencyApiService()
        CurrencyService.create_by_api_data(api_service)

    return render(request, 'currency-importer.html', {})
