from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='search'),
    path('about',views.about_page,name='about'),
    path('phone/<int:id>/', views.PhoneDetailView, name='phone-details'),
]
