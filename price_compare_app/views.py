from django.shortcuts import render

from .models import Phone

# Create your views here.

def home_page(request):
    phones = Phone.objects.all()
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

    return render(request, 'index.html',  {"context": context, "phones": phones})


def about(request):
    return render(request, 'about.html')

 


