from django.urls import path

from . import views

urlpatterns = [
    path("add-item/", views.AddItemToCartView.as_view(), name="additem"),
    path("remove-item/<int:itemid>", views.RemoveItemFromCartView.as_view(),
                    name="removeitem"),
    path("view-cart/", views.ShoppingCartDetailView.as_view(), name="viewcart"),
]