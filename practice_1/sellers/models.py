from django.db import models


class Sellers(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    # products = models.ManyToManyField(Products)

    def __str__(self) -> str:
        return self.name
