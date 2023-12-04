from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name: models.CharField = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Details(models.Model):
    name: models.CharField = models.CharField(max_length=200)
    description: models.TextField = models.TextField()
    model: models.CharField = models.CharField(
        max_length=150, null=True, blank=True
    )


class Products(models.Model):
    name: models.CharField = models.CharField(max_length=150)
    brand: models.CharField = models.CharField(max_length=150)
    price: models.PositiveIntegerField = models.PositiveIntegerField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    updated_at: models.DateTimeField = models.DateTimeField(
        blank=True, null=True
    )
    # details = models.OneToOneField(Details)
    # category = models.ManyToManyField(Category),
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
