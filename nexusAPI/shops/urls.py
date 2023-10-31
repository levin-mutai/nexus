from django.urls import path
from .views import *

urlpatterns = [
    path(
        "/products",
        ProductViewSet.as_view({"get": "get_queryset","post":"create"}),
    ),
    path(
    "/products/<pk>",
    ProductViewSet.as_view({"get":"retrieve","put": "update", "delete": "destroy"}),
),
    path(
        "/staffs",
        StaffViewSet.as_view({"get": "get_queryset","post":"create"}),
    ),
    path(
    "/staffs/<pk>",
    StaffViewSet.as_view({"get":"retrieve","put": "update", "delete": "destroy"}),
),
    path(
        "",
        ShopViewSet.as_view({"get": "myshops","post":"create"}),
    ),
    path(
    "/<pk>",
    ShopViewSet.as_view({"get":"retrieve","put": "update", "delete": "destroy"}),
),
]
