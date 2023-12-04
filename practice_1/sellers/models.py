from django.db import models

# from products.models import Products


class Sellers(models.Model):
    name: models.CharField = models.CharField(max_length=150)
    address: models.TextField = models.TextField()
    phone: models.CharField = models.CharField(max_length=11)
    banck_account: models.CharField = models.CharField(max_length=100)
    # products = models.ManyToManyField(Products)

    def __str__(self) -> str:
        return self.name
