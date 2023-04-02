from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer, OfferSerializer


class LatestProductsList(APIView):
    permission_classes = []

    @extend_schema(tags=['Products - Public'], responses=ProductSerializer)
    def get(self, request, format=None):
        products = Product.objects.all()[0:3]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class OfferProduct(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Products - Public'], request=OfferSerializer, responses=None)
    def post(self, request):
        product = Product.objects.get(id=request.data['id'])
        if product.price < request.data['price']:
            product.price = request.data['price']
            product.save()
        else:
            return Response(
                data={'message': 'Offer price must be higher than current price'},
                status=status.HTTP_400_BAD_REQUEST)
        return Response( 
            data={'message': 'Offer accepted'},
            status=status.HTTP_200_OK)


