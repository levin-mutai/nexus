from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
from .serializers import *
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .permisions import IsStaffPermission
from .utils import Authorization

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    '''This a view used to perform all product related actions in the shop'''
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffPermission]

    def get_queryset(self):
        """Used to get all the products available"""
        queryset = Products.objects.all()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def create(self, request, *args, **kwargs):
        """Used to add new products to the shop"""
        serializer = self.get_serializer(data=request.data)
        auth =Authorization.check_admin_or_staff_authorization(request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self,request,pk=None,*args, **kwargs):
        """Used to get specific shops available"""
        queryset = Products.objects.get(id = pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def list(self,request,*args, **kwargs):
        """Used to get all the shops available"""
        queryset = Shops.objects.all()
        shop_name = self.request.query_params.get('shop_name')
        if shop_name:
            queryset = queryset.filter(shop_name=shop_name)
            return Response(ShopSerializer(queryset).data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request,pk=None, *args, **kwargs):
        """Used to update the products in the shop"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        auth =Authorization.check_admin_or_staff_authorization(request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request,pk=None, *args, **kwargs):
        """Used to delete the products in the shop"""
        instance = self.get_object()
        auth =Authorization.check_admin_or_staff_authorization(request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        """Used to get all the shops available"""
        queryset = Shops.objects.all()
        return queryset
    def myshops(self,request,*args, **kwargs):
        """Used to get all the shops registered under the person making request"""
        try:
            queryset = Shops.objects.filter(owner = request.user.id).all()


            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Shops.DoesNotExist:
            return Response({"error":"You do not have any shop registered under your account"},status=status.HTTP_404_NOT_FOUND)
    def retrieve(self,request,pk=None,*args, **kwargs):
        """Used to get specific shops available"""
        queryset = Shops.objects.get(id = pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Used to add new shops to the shop"""
        user = request.user.id
        request.data["owner"] = user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request,pk=None, *args, **kwargs):
        """Used to update the shops in the shop"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        auth =Authorization.check_admin_authorization(pk,request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request,pk=None, *args, **kwargs):
        """Used to delete the shops in the shop"""
        instance = self.get_object()
        auth =Authorization.check_admin_authorization(pk,request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffViewSet(viewsets.ModelViewSet):
    '''This a view used to perform all staff related actions in the shop'''

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        """Used to get all the staffs available"""
        queryset = Staff.objects.all()
        shop_id = self.request.query_params.get('shop_id')
        if shop_id:
            queryset = queryset.filter(shop=shop_id)
        return queryset

    def create(self, request, *args, **kwargs):
        """Used to add new staffs to the shop"""
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            res =StaffSerializer.create(request.data)
            return Response(StaffSerializer(res), status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None,*args, **kwargs):
        """Used to get all the shops available"""
        queryset = Staff.objects.get(shop=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request,pk=None, *args, **kwargs):
        """Used to update the staffs in the shop"""
        partial = False
        instance = self.get_object()
        auth =Authorization.check_admin_authorization(shop_id=request.data.shop,request= request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def destroy(self, request,pk=None, *args, **kwargs):
        """Used to delete the staffs in the shop"""
        instance = self.get_object()
        auth =Authorization.check_admin_authorization(shop_id=request.data.shop,request= request)
        if not auth:
            return Response({"error":"you are not authorized to perform this action"},status=status.HTTP_403_FORBIDDEN)
        StaffSerializer.destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
