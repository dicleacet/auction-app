from django.db.models import Q
from django.http import Http404
from product.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product

class LatestProductsList(APIView):
    permission_classes = []

    def get(self, request, format=None):
        products = Product.objects.all()[0:3]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


