from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('about/',views.about_page,name='about'),
    # path('phone/<slug:slug>/', views.PhoneDetailView, name='phone'),
]
 