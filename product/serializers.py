from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'get_image', 'get_thumbnail', 'price' , 'description'
        ]

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'price'  
        ]
