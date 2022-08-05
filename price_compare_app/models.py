from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=200, null=False, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default-product.png', blank=True)
    url_jumia = models.URLField(max_length=9999, db_index=True)
    url_konga = models.URLField(max_length=9999, db_index=True)
    price_jumia = models.DecimalField(max_digits=8, decimal_places=2,null=False,default=0)
    price_konga = models.DecimalField(max_digits=8, decimal_places=2,null=False,default=0)
    star_reviews=models.DecimalField(max_digits=2,decimal_places=1,null=True)

    def get_jumia_price(self):
        price = int(self.price_jumia)
        return f"₦{price}"

    def get_konga_price(self):
        price = int(self.price_konga)
        return f"₦{price}"

    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return self.name

class WishList(models.Model):
    phone =models.ForeignKey(Phone,on_delete=models.SET_NULL, null=True, blank=True) 
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    date_listed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} wishlist"

class Review(models.Model):
    comment = models.TextField(max_length=100000,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone= models.ForeignKey(Phone,on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return f"{self.user} comment on {self.phone}"
