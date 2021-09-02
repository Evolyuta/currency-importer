from app.models import Currency

from .core_repository import CoreRepository


class CurrencyRepository(CoreRepository):
    model = Currency
