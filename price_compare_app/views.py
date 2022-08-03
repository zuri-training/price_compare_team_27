from django.shortcuts import render

from price_compare_app.models import *
from pyexpat import model
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from price_compare_app.models import Phone

# Create your views here.

def home_page(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_phone = Phone.objects.filter(name__icontains=q)
    
    else:
        all_samsung= Phone.objects.filter(brand__name__icontains='samsung')
        all_iphones= Phone.objects.filter(brand__name__icontains='iphone')
        all_huawei= Phone.objects.filter(brand__name__icontains='huawei')


    context={
        'iphones':all_iphones,
        'samsung':all_samsung,
        'huawei':all_huawei
    }

    return render(request,'price_compare_app/index.html',context)

def wishlist(request):
    if request.user.is_authenticated:
        user = request.user.id

        wishes, created= WishList.objects.get_or_create(user_id=user)
        items = wishes.wishitem_set.all()
        best_price = WishItem.objects.all()
    else:
        # items = []
        # wishes = {'get_cart_total': 0, 'get_cart_items':0, 'best_price':0}
        return render(request, 'price_compare_app/index.html')
    context = {
        'items':items, 'wish': wishes, 'best_price': best_price
    }
        
    return render(request, 'price_compare_app/wishlist.html', context)




def about_page(request):
    return render(request,'price_compare_app/about.html')


def PhoneDetailView(request, slug):
    item = get_object_or_404(Phone, slug = slug)

    return render(request, 'price_compare_app/index.html', context={'item': item})
    