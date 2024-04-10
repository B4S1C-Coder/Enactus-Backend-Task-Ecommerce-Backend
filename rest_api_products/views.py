from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from knox.auth import TokenAuthentication

from .models import Product
from .serializers import ProductSerializer

# POST
class CreateProductView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser,]
    queryset = Product.objects.all()

# GET, PUT/PATCH, DELETE
class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser,]
    queryset = Product.objects.all()
