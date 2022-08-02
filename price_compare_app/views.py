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


def PhoneDetailView(request, slug):
    item = get_object_or_404(Phone, slug = slug)

    return render(request, 'price_compare_app/index.html', context={'item': item})