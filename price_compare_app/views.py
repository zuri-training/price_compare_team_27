from django.shortcuts import render, redirect

from price_compare_app.models import Phone


# Create your views here.

def home_page(request):
    return render(request,'price_compare_app/index.html')



def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            phone = Phone.objects.filter(name_icontains=q)
            return render(request, 'search.html', {'phone': phone})
        else:
            print("not available")
            return render(request, 'search.html', {})
