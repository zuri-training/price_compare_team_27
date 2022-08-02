from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('phone/<slug:slug>/', views.PhoneDetailView, name='phone'),
]
