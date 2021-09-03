from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=120)
    code = models.CharField(max_length=120, null=True)

    # Many-to-many relationship to itself
    compared_currencies = models.ManyToManyField(
        'self',
        through='CurrencyComparison',
        symmetrical=False,
        related_name='compared_to'
    )

    class Meta:
        # Plural model label name
        verbose_name_plural = 'Currencies'


class CurrencyComparison(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    ratio = models.FloatField()

    # Getting title of comparing currency
    def currency_title(self):
        return self.from_currency.title

    # Getting title of compared currency
    def compared_currency_title(self):
        return self.to_currency.title

    class Meta:
        # Singular model label name
        verbose_name = 'Currency comparison'
