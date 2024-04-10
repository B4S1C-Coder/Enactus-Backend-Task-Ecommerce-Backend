from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

from knox.auth import TokenAuthentication

from rest_api_products.models import Product
from rest_api_products.serializers import ProductSerializer

from .models import ShoppingCart, ShoppingCartItem
from .serializers import (
    ShoppingCartSerializer, ShoppingCartItemSerializer
)

# class ShoppingCartDetailView(generics.RetrieveAPIView):
#     queryset = ShoppingCart.objects.all()
#     serializer_class = ShoppingCartSerializer
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [permissions.IsAuthenticated,]

class ShoppingCartDetailView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):

        cart = ShoppingCart.objects.filter(user_id=request.user.id).first()

        if cart:
            cart_serializer = ShoppingCartSerializer(cart)

            # cart_item_serializer = ShoppingCartItemSerializer(cart.shoppingcartitem_set.all(), many=True)
            
            result = dict(cart_serializer.data)
            result['cart_items'] = []

            for item in cart.shoppingcartitem_set.all():
                result['cart_items'].append(dict(ProductSerializer(item.product).data))


            return Response(result,
                            status=status.HTTP_200_OK)
        
        return Response({"detail": "Couldn't find shopping cart."}, status=status.HTTP_400_BAD_REQUEST)

class AddItemToCartView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        cart_item_serializer = ShoppingCartItemSerializer(data=request.data)

        if cart_item_serializer.is_valid():
            # Find the associated shopping cart
            shopping_cart = ShoppingCart.objects.filter(user=request.user).first()

            if not shopping_cart:
                return Response({"detail": "Couldn't find shopping cart."},
                            status=status.HTTP_400_BAD_REQUEST)
            
            product = cart_item_serializer.validated_data['product']

            # Check if sufficient quantity is available in stock
            if product.inventory_level < cart_item_serializer.validated_data['quantity']:
                return Response({"detail": "Insufficent inventory level."},
                            status=status.HTTP_400_BAD_REQUEST)

            # Save the newly added item and update the inventory levels
            product = Product.objects.filter(id=product.id).first()
            print(f"[DEBUG] {product}")
            quantity = cart_item_serializer.validated_data['quantity']
            product.inventory_level -= quantity
            product.save()
            cart_item = cart_item_serializer.save(shopping_cart=shopping_cart)

            return Response(cart_item_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveItemFromCartView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request, itemid):

        # Find the associated shopping cart
        shopping_cart = ShoppingCart.objects.filter(user=request.user).first()

        if not shopping_cart:
            return Response({"detail": "Couldn't find shopping cart."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the given itemid is associated with the shopping cart
        item = shopping_cart.checkIfItemID_isAssociated(id=itemid)
        if item:
            # update inventory levels
            item.product.inventory_level += item.quantity
            item.product.save()
            item.delete()

            return Response({"detail": "Item removed from cart."},
                                status=status.HTTP_200_OK)

        else:
            return Response({"detail": "Specified item does not exist in the cart"},
                            status=status.HTTP_400_BAD_REQUEST)
