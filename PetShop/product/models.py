from django.db import models


class Product(models.Model):
    # название продукта
    nomination = models.CharField(max_length=64)
    # стоимость продукта
    price = models.IntegerField(default=0)
    # картинка
    image = models.ImageField(upload_to='images/products', null=True, blank=True)

class Food(Product):
    # "изготовлено"
    manufacture_date = models.DateTimeField()
    # "годен до"
    expiration_date = models.DateTimeField()
    # кому
    for_animal_kind = models.CharField(max_length=16)
    # вид еды/корма
    type = models.CharField(max_length=16)
