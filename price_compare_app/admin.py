from django.contrib import admin

from .models import Brand, Phone, Review, WishItem, WishList

# Register your models here.



class BrandManager(admin.ModelAdmin):
    list_filter=['name']
    search_fields = ["name"]

class PhoneManager(admin.ModelAdmin):
    list_filter=['brand','created_on']
    search_fields = ["name","brand"]

class ReviewManager(admin.ModelAdmin):
    list_filter=['phone']




admin.site.register(Brand, BrandManager)
admin.site.register(Phone,PhoneManager)
admin.site.register(Review,ReviewManager)
admin.site.register(WishList)
admin.site.register(WishItem)