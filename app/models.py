from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=120)
    code = models.CharField(max_length=120, null=True)

    compared_currencies = models.ManyToManyField(
        'self',
        through='CurrencyCompare',
        symmetrical=False,
        related_name='compared_to'
    )


class CurrencyCompare(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    ratio = models.FloatField()
