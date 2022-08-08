from django.contrib import admin

from .models import Brand, Phone, Review, WishList,WishItem
# Register your models here.



class BrandManager(admin.ModelAdmin):
    list_filter=['name']
    search_fields = ["name"]



admin.site.register(Brand, BrandManager)
admin.site.register(Phone)
admin.site.register(Review)
admin.site.register(WishList)
admin.site.register(WishItem)