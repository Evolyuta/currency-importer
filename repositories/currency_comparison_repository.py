from app.models import CurrencyComparison

from .core_repository import CoreRepository


class CurrencyComparisonRepository(CoreRepository):
    model = CurrencyComparison
