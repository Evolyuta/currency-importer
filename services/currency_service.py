import itertools

from normalizers.currency_normalizer import CurrencyNormalizer
from repositories.currency_comparison_repository import CurrencyComparisonRepository
from repositories.currency_repository import CurrencyRepository
from services.currency_api_service import CurrencyApiService


class CurrencyService:
    api_service = None
    currency_repository = None
    currency_comparison_repository = None

    def __init__(self):
        self.api_service = CurrencyApiService()
        self.currency_repository = CurrencyRepository()
        self.currency_comparison_repository = CurrencyComparisonRepository()

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

    # Importing currency comparison list by data from api
    def import_currency_comparison_list(self):
        currency_repository = self.currency_repository
        currency_comparison_repository = self.currency_comparison_repository

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

                        currency_comparison = currency_comparison_repository.get(
                            from_currency_id=currency_id,
                            to_currency_id=compared_currency_id
                        )

                        if not currency_comparison:
                            currency_comparison_repository.create(
                                from_currency_id=currency_id,
                                to_currency_id=compared_currency_id,
                                ratio=ratio
                            )
                        elif ratio != currency_comparison.ratio:
                            currency_comparison_repository.update(
                                instance_id=currency_comparison.id,
                                ratio=ratio,
                            )
