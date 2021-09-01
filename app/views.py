from django.shortcuts import render


def currency_importer_view(request, *args, **kwargs):
    return render(request, 'currency-importer.html', {})
