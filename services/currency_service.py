from json import JSONDecodeError

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

    # Importing currency comparison list by data from api
    def import_currency_comparison_list(self):
        currency_repository = self.currency_repository
        currency_comparison_repository = self.currency_comparison_repository

        currencies = currency_repository.get_list()

        errors = []

        for currency in currencies:
            currency_code = currency.code
            currency_code_lower = currency_code.lower()

            try:
                api_currency_ratios = self.api_service.get_ratios_for_currency(currency_code_lower)

                compared_currencies = currency_repository.get_list()

                for compared_currency in compared_currencies:
                    compared_currency_code_lower = compared_currency.code.lower()

                    if compared_currency_code_lower != currency_code_lower:

                        if api_currency_ratios.get(compared_currency_code_lower):
                            ratio = api_currency_ratios[compared_currency_code_lower]

                            compared_currency_id = compared_currency.id
                            currency_id = currency.id

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

            except JSONDecodeError:
                errors.append(f'Api request error for currency with code "{currency_code}"')

        return errors
