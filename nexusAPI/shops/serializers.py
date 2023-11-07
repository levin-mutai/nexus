from rest_framework import serializers
from .models import Shops,Products,Staff
from accounts.models import User
import logging


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ('id',"created_at","updated_at")
        extra_kwargs = {
            'shop_id': {'required': True}
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ('id',"created_at","updated_at")


        def create(self, validated_data):
            user_id = validated_data["user"]
            user = User.objects.get(id=user_id)
            user.is_staff = True
            user.save()
            try:
                instance = Staff.objects.create(**validated_data)
                logging.info(f"created a new staff with ID of {instance.id} for shop {instance.shop.name}")
                return instance
            except Exception as e:
                raise serializers.ValidationError(e)

        def destroy(self, instance):
            user_id = instance.user
            is_staff = Staff.objects.filter(user=user_id)
            if not is_staff:
                user = User.objects.get(id=user_id)
                user.is_staff = False
                user.save()

            logging.info(f"removed staff with ID of {instance.id} from shop {instance.shop.name}")
            instance.delete()


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
        read_only_fields = ('id',"created_at","updated_at")
        extra_kwargs = {
            'owner': {'required': False}
        }

