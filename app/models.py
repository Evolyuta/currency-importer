from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=120)
