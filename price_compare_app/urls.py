from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('wishlist', views.wishlist, name='wishlist')
]
 