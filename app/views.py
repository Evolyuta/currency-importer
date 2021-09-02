from django.shortcuts import render

from services.currency_service import CurrencyService


def currency_importer_view(request):
    context = {}
    currency_service = CurrencyService()

    if request.method == 'POST':

        currency_service.import_currency_list()
        currency_service.import_currency_compare_list()
    else:
        context = {
            "object_list": currency_service.get_data_for_compare_view()
        }

    return render(request, 'currency-importer.html', context)
