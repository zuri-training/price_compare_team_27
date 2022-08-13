from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page,name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('search/',views.search,name='search'),
    path('about/',views.about_page,name='about'),
    path('phone/<int:id>/', views.PhoneDetailView, name='phone-details'),
    path('contact/', views.contact, name='contact'),
    path('documentation/', views.documentation, name='doc'),
    path('documentation-features/',views.documentation_features, name='doc-features'),
    path('documentation-signup/',views.documentation_sign_up, name='doc-sign'),
    path('documentation-compare/',views.documentation_compare_prices, name='doc-compare'),
    path('documentation-search/',views.documentation_search, name='doc-search'),
    path('iphone13/',views.iphone13, name='iphone13'),

]
 
 
