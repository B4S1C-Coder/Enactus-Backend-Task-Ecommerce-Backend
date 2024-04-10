from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateProductView.as_view(), name="createproduct"),
    path("alter/<int:pk>", views.RetrieveUpdateDestroyProductView.as_view(),
                    name="alterproduct"),
]