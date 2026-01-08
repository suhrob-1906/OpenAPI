from django.urls import path

from .views import ProductListCreateView, ProductRetrieveDestroyView

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path(
        "products/<int:pk>/",
        ProductRetrieveDestroyView.as_view(),
        name="product-detail",
    ),
]
