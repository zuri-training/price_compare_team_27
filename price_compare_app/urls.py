from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('search',views.search,name='search'),
    path('about',views.about_page,name='about'),
    path('phone/<int:id>/', views.PhoneDetailView, name='phone-details'),
]
 