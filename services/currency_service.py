import itertools

from normalizers.currency_normalizer import CurrencyNormalizer
from repositories.currency_compare_repository import CurrencyCompareRepository
from repositories.currency_repository import CurrencyRepository
from services.currency_api_service import CurrencyApiService


class CurrencyService:
    api_service = None
    currency_repository = None
    currency_compare_repository = None

    def __init__(self):
        self.api_service = CurrencyApiService()
        self.currency_repository = CurrencyRepository()
        self.currency_compare_repository = CurrencyCompareRepository()

    # Importing currency list by data from api
    def import_currency_list(self):
        api_data = self.api_service.get_all_currencies()
        currency_data_normalized = CurrencyNormalizer.normalize(api_data)
        currency_repository = self.currency_repository

        for currency_item_normalized in currency_data_normalized:
            title = currency_item_normalized['title']
            code = currency_item_normalized['code']

            currency = currency_repository.get(code=code)

            if not currency:
                currency_repository.create(
                    title=title,
                    code=code,
                )
            elif title != currency.title:
                currency_repository.update(
                    instance_id=currency.id,
                    title=title,
                )

    # Importing currency compare list by data from api
    def import_currency_compare_list(self):
        currency_repository = self.currency_repository
        currency_compare_repository = self.currency_compare_repository

        currencies = currency_repository.get_list()

        for currency in currencies:
            currency_code = currency.code

            api_currency_ratios = self.api_service.get_ratios_for_currency(currency_code)[currency_code]
            api_currency_ratios = dict(itertools.islice(api_currency_ratios.items(), 2))

            for compared_currency_code in api_currency_ratios:
                if compared_currency_code != currency_code:
                    compared_currency = currency_repository.get(code=compared_currency_code)

                    if compared_currency:
                        compared_currency_id = compared_currency.id
                        currency_id = currency.id
                        ratio = api_currency_ratios[compared_currency_code]

                        currency_compare = currency_compare_repository.get(
                            from_currency_id=currency_id,
                            to_currency_id=compared_currency_id
                        )

                        if not currency_compare:
                            currency_compare_repository.create(
                                from_currency_id=currency_id,
                                to_currency_id=compared_currency_id,
                                ratio=ratio
                            )
                        elif ratio != currency_compare.ratio:
                            currency_compare_repository.update(
                                instance_id=currency_compare.id,
                                ratio=ratio,
                            )

    # Getting data for currency compare view
    def get_data_for_compare_view(self):
        currency_repository = self.currency_repository

        currency_compare_list = self.currency_compare_repository.get_list()
        currency_compare_list_view = []

        for currency_compare_item in currency_compare_list:
            currency = currency_repository.get(id=currency_compare_item.from_currency_id)
            currency_compared = currency_repository.get(id=currency_compare_item.to_currency_id)
            ratio = currency_compare_item.ratio

            currency_compare_list_view.append({
                'currency_title': currency.title,
                'currency_compared_title': currency_compared.title,
                'ratio': ratio,
            })

        return currency_compare_list_view
