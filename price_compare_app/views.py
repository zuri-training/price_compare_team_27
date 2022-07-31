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



<<<<<<< HEAD
def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            phone = Phone.objects.filter(name__icontains=q)
            return render(request, 'search.html', {'phone': phone})
        else:
            print("not available")
            return render(request, 'search.html', {})
=======
>>>>>>> f0ff6df35ebba9df5185414dfcddfd91f9d224e6
