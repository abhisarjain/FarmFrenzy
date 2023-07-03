from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
class Profile(AbstractUser):
    bio = models.TextField()
    is_seller = models.BooleanField(default=False)

    def is_sellerornot(self):
        return self.is_seller
    
@receiver(post_save, sender=Profile)
def create_profile_related_models(sender, instance, created, **kwargs):
    if created:
        if instance.is_seller:
            Seller.objects.create(user=instance)
        else:
            Buyer.objects.create(user=instance)
    else:
        if instance.is_seller:
            Seller.objects.update_or_create(user=instance)
        else:
            Buyer.objects.update_or_create(user=instance)

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

class Crop(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    shelf_life = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

class Negotiation(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    proposed_price =  models.IntegerField(default=0)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    awaited = models.BooleanField(default=True)
    bought = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.crop.name



class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    quantity_bought = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.crop.name 
# class Order(models.Model):
#     buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderItem')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order #{self.id} - Buyer: {self.buyer.user.username}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.product.name} - Quantity: {self.quantity}"
