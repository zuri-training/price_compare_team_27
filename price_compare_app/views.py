from django.shortcuts import get_object_or_404, render

from price_compare_app.models import Phone

# Create your views here.

def get_random_four():
    pass

def get_latest_four():
    pass

def home_page(request):
    all_samsung= Phone.objects.all
    all_iphones= Phone.objects.all
    all_huawei= Phone.objects.all


    context={
        'iphones':all_iphones,
        'samsung':all_samsung,
        'huawei':all_huawei
    }

    return render(request,'price_compare_app/landingpage.html')

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        return render(request, 'price_compare_app/search.html', {'query':query})
    else:
        return render(request, 'price_compare_app/search.html', {'query':query})




def about_page(request):
    return render(request,'price_compare_app/about.html')


def PhoneDetailView(request, slug):
    item = get_object_or_404(Phone, slug = slug)

    return render(request, 'price_compare_app/index.html', context={'item': item})
    
