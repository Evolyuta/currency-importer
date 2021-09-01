from app.models import Currency

from .model_service import ModelService


class CurrencyService(ModelService):
    model = Currency
