
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NexusAPI",
        default_version="v1",
        description="""This is an API for nexis. It is a challange given by PEER Carbon.\n\n For you to use this API you need to first login. You can do that using the user login route(user/login). If not yet a user please register using the user register route(user/register).\n\n After successful login you will get both `access` and `refresh` token. You will need the `access` token for **Authorization**\n\nIf using curl or any other tool make sure to pass `Authorization` as a header with a value of the Bearers token e.g \n\n ```curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2MzY5MTc2LCJpYXQiOjE2OTYzNjE5NzYsImp"``` """,
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="levinmutai@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", include("accounts.urls")),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path(
        "",
        include_docs_urls(
            title="NexusAPI",
            description="""This is an API for nexis. It is a challange given by PEER Carbon. \n\n For you to use this API you need to first login. You can do that using the user login route(user/login). If not yet a user please register using the user register route(user/register).\n\n After successful login you will get both `access` and `refresh` token. You will need the `access` token to access any route in this API.\n\n To do that, copy the `access` token obtained, then click on `Authenticatiion` on the left bottom of the screen then select `token` then paste the token on the **Token** field and on **Scheme** please use 'Bearer' then click on **USe Token Authentication** and just like that you can test the endpoinps!\n\nIf using curl or any other tool make sure to pass `Authorization` as a header with a value of the Bearers token e.g \n\n ```curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2MzY5MTc2LCJpYXQiOjE2OTYzNjE5NzYsImp"```\n\n**Note:** If you prefer *swagger* for documentation please head to `/swagger` and `/redoc` for *redoc*.
                """,
        ),
    ),
]
