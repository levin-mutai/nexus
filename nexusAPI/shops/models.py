from django.db import models
import uuid
from accounts.models import User



class BaseModel(models.Model):
    id = models.CharField(
        max_length=100, primary_key=True, unique=True, default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shops(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    logo = models.ImageField(upload_to='shops',null=True,blank=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def get_products(self):
        return self.product_set.all()

    def get_staff(self):
        return self.staff_set.all()

class Categories(models.Model):
    category = models.CharField(max_length=100, primary_key=True)

class Products(BaseModel):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL, null=True)
    stock = models.PositiveIntegerField()
    measurement = models.CharField(max_length=100, default="units")

class Staff(BaseModel):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['shop']
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        unique_together = ('shop', 'user')
        get_latest_by = 'created_at'
        indexes = [
            models.Index(fields=['shop', 'user']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['shop', 'user'], name='unique_staff')
        ]

