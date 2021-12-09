from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)  # имя товара
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be >= 0')])  # количество товара на складе
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name} {self.quantity}'


# категории товаров: именно на них ссылается модель товара
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'