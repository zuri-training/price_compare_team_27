from django.shortcuts import get_object_or_404, render

from price_compare_app.models import Phone

# Create your views here.

def get_random_four():
    pass

def get_latest_four():
    pass

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

    return render(request,'price_compare_app/landingpage.html',context)



def about_page(request):
    return render(request,'price_compare_app/about.html')


def PhoneDetailView(request, slug):
    item = get_object_or_404(Phone, slug = slug)

    return render(request, 'price_compare_app/index.html', context={'item': item})
    