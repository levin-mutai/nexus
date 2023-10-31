from .models import Staff,Shops
from django.http import request
import logging

from .custom_errors import ShopDoesNotExistError


class Authorization:

    def is_owner(user_id, shop_id):
        try:
            shop = Shops.objects.get(pk=shop_id)
            return shop.owner.id == user_id
        except ShopDoesNotExistError:
            logging.error("Shop with ID %s does not exist.", shop_id)
            return False

    @classmethod
    def check_admin_or_staff_authorization(cls,request = request):
        """
        This function checks if the user is allowed to perform actions on products
        """
        user_id = request.user.id
        shop_id = request.data.shop

        if  Staff.objects.filter(user=user_id,shop=shop_id).exists():
            return True
        return cls.is_owner(user_id,shop_id)

    @classmethod
    def check_admin_authorization(cls,shop_id,request = request):
        """
        This function checks if the user is allowed to perform actions on the shop
        """
        user_id = request.user.id

        return cls.is_owner(user_id,shop_id)

