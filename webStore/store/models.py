from django.conf import settings
from django.db import models
from email.policy import default
from setuptools._vendor import ordered_set
from random import choices
from _datetime import timezone
from django.views.generic.dates import timezone_today


CATEGORY_CHOICES = (
    ('S', 'Camisa'),
    ('SW', 'Camiseta'),
    ('OW', 'Otra prenda'),
    )

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secundary'),
    ('D', 'danger'),
    )


class Item(models.Model):
    tittle = models.CharField(max_length = 100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, default='S', max_length = 3)
    label = models.CharField(choices=LABEL_CHOICES, default='P', max_length = 1)
    
    def __str__(self):
        return self.tittle


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.tittle

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(timezone_today)
    
    def __str__(self):
        return self.user.username
