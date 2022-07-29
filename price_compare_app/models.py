
from django.contrib.auth.models import User
from django.db import models
from django.forms import BooleanField
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, db_index=True)
    email = models.CharField(max_length=200, null=True, db_index=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=200, null=True, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, db_index=True)
    price = models.FloatField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)

    url_jumia = models.CharField(max_length=250, db_index=True)
    url_konga = models.CharField(max_length=250, db_index=True)


    price_jumia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price_komga = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    
    class Meta:
        ordering = ('name')
    

    def get_absolute_url(self):
        return reverse('price_compare_app:scrape', args=[self.slug])

    def __str__(self):
        return self.name

class WishList(models.Model):
    phone =models.ForeignKey(Phone,on_delete=models.SET_NULL, null=True, blank=True) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    date_listed = models.DateTimeField(auto_now_add=True)
    wish_id = models.CharField(max_length=100, null=True, db_index=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return str(self.id)

class Order(models.Model):
     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
     date_ordered = models.DateTimeField(auto_now_add=True)
     complete = models.BooleanField(default=False, null=True, blank=False)
     transaction_id = models.CharField(max_length=200, null=True)

     def __str__(self):
        return str(self.id)