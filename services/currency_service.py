from normalizers.currency_normalizer import CurrencyNormalizer
from repositories.currency_repository import CurrencyRepository


class CurrencyService:
    @staticmethod
    def create_by_api_data(api_service):
        currency_repository = CurrencyRepository()

        api_data = api_service.get_all_currencies()
        currency_data_normalized = CurrencyNormalizer.normalize(api_data)

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
