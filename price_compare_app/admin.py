from django.contrib import admin

from .models import Brand, Phone, Review, WishList

# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# class BrandManager(admin.ModelAdmin):
#     list_filter=['name']
#     search_fields = ["name"]

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'created_on', 'url_jumia', 'url_konga')
    list_filter = ('created_on', 'brand')
    search_fields = ('brand',)
    ordering = ('created_on',)


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user', 'date_listed')
    list_filter = ('phone', 'date_listed')
    search_fields = ('phone',)
    raw_id_fields = ('user',)
    ordering = ('date_listed',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'phone')
    list_filter = ('phone',)
    search_fields = ('phone',)
    ordering = ('phone',)
