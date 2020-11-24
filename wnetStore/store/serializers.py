from rest_framework import serializers
from store.models import Product
from store.models import Customer

# from store.models import Order, OrderItem, ShippingAddress
from drf_extra_fields.fields import Base64ImageField


class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Product
        fields = ('name','price','digital','image')


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('user','name','email')
