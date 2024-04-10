from rest_framework import generics
from rest_framework import permissions
from knox.auth import TokenAuthentication

from .models import Supplier
from .serializers import SupplierSerializer

# POST
class CreateSupplierView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

# GET, PUT/PATCH, DELETE
class RetrieveUpdateDestroySupplierView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()