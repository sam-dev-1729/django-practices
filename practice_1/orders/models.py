from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Orders(models.Model):
    owner: models.ForeignKey = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # owner
    price: models.PositiveIntegerField = models.PositiveIntegerField()
    description: models.TextField = models.TextField()
    date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
