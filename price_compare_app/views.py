from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'price_compare_app/index.html')



def search():
    pass

