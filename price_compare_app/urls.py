from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('',views.home_page,name='home'),
    path('about',views.about_page,name='about'),
=======
    path('',views.home_page,name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('search/',views.search,name='search'),
    path('about/',views.about_page,name='about'),
>>>>>>> 74e71b37e7d6af326b8296b06c2b405f637438d6
    path('phone/<int:id>/', views.PhoneDetailView, name='phone-details'),
    path('contact/', views.contact, name='contact'),
    path('categories/', views.categories, name='categories'),
    path('samsung-category/', views.samsung_category, name='samsung'),
    path('tecno-category/', views.tecno_category, name='tecno'),
    path('xiaomi-category/', views.xiaomi_category, name='xiaomi'),
    path('oppo-category/', views.oppo_category, name='oppo'),
    path('infinix-category/', views.infinix_category, name='infinix'),
    path('documentation/', views.documentation, name='doc'),
    path('documentation-features/',views.documentation_features, name='doc-features'),
    path('documentation-signup/',views.documentation_sign_up, name='doc-sign'),
    path('documentation-compare/',views.documentation_compare_prices, name='doc-compare'),
    path('documentation-search/',views.documentation_search, name='doc-search'),
    path('iphone13/',views.iphone13, name='iphone13'),

]
 
 
