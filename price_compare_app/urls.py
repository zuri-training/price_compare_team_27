from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('about',views.about_page,name='about'),
<<<<<<< HEAD
    path('phone/<int:id>/', views.PhoneDetailView, name='phone-details'),
=======
    path('phone/<slug:slug>/', views.PhoneDetailView, name='phone'),
    path('search',views.search,name='search'),

>>>>>>> c45b229fd6175c010461200b59d1a1ab3448d2ff
]
