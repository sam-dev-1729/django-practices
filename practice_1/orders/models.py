from django.contrib.auth import get_user_model
from django.db import models
from products.models import Products

User = get_user_model()


class Orders(models.Model):
    owner: models.ForeignKey = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    products: models.ForeignKey = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
    )
    quantity: models.IntegerField = models.IntegerField()
    price: models.PositiveBigIntegerField = models.PositiveBigIntegerField()
    description: models.TextField = models.TextField()
    date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
