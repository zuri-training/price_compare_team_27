from django.shortcuts import render

from price_compare_app.models import Phone

# Create your views here.

def home_page(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_phone = Phone.objects.filter(name__icontains=q)
    
    else:
        all_phone= Phone.objects.all()
    context={
        'phones':all_phone
    }

    return render(request,'price_compare_app/index.html',context)



