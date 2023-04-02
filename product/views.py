from django.db.models import Q
from django.http import Http404
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:3]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_slug):
        try:
            return Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_slug, format=None):
        product = self.get_object( product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

