from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateSupplierView.as_view(), name="createsupplier"),
    path("alter/<int:pk>", views.RetrieveUpdateDestroySupplierView.as_view(),
                    name="altersupplier"),
]