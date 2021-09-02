from app.models import CurrencyCompare

from .core_repository import CoreRepository


class CurrencyCompareRepository(CoreRepository):
    model = CurrencyCompare
