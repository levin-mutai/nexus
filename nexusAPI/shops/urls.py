from django.urls import path
from .views import *

urlpatterns = [
    path(
        "/products",
        ProductViewSet.as_view({"get": "get_queryset","post":"create"}),
    ),
    path(
    "/products/<int:pk>",
    ProductViewSet.as_view({"put": "update", "delete": "destroy"}),
),
    path(
        "/staffs",
        StaffViewSet.as_view({"get": "get_queryset","post":"create"}),
    ),
    path(
    "/staffs/<int:pk>",
    StaffViewSet.as_view({"put": "update", "delete": "destroy"}),
),
    path(
        "",
        ShopViewSet.as_view({"get": "get_queryset","post":"create"}),
    ),
    path(
    "/<int:pk>",
    ShopViewSet.as_view({"put": "update", "delete": "destroy"}),
),
]
