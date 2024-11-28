from django.db import models
from django.conf import settings

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASECADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"cart of {self.user.email}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASECADE, related_name='item')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASECADE)
    quentity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quentity} * {self.menu_item.name}"