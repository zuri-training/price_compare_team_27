import json
import random

from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from price_compare_app.form import ContactForm, ReviewForm
from price_compare_app.models import *

from .form import ReviewForm
from .models import Phone


def get_random_item():
    pass

def home_page(request): 
    popular_phones = Phone.objects.order_by('?')[:8]

    latest_phones = Phone.objects.order_by('-modified_on')[:4]

    context={
        'phones':popular_phones,   
        'latest_phone':latest_phones  
    }
    return render(request,'price_compare_app/landingpage.html',context)


@login_required(login_url='login')
def wishlist(request):
    user = request.user.id
    wishes, created= WishList.objects.get_or_create(user_id=user)
    items = wishes.wishitem_set.all()
    best_price = WishItem.objects.all()
    context = {
        'items':items, 'wish': wishes, 'best_price': best_price
    }
        
    return render(request, 'price_compare_app/wish.html', context)


def search(request):
    if 'search' in request.GET:
        search_keyword=request.GET['search']
        if search:
            phones=Phone.objects.filter(name__icontains=search_keyword)
     
   
        context={
            'phones':phones,
        }
        
        return render(request,'price_compare_app/search.html',context)
    else:
        print('No search result found')
        return render(request,'price_compare_app/search.html',{})


def about_page(request):
    return render(request,'price_compare_app/about.html')

def updateItem(request):
    # loads the data from the wishlist.js javascript file and creates variables to store this data in productId is the phoneId
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # retrieves the user based on the user_id and retrieves products based on productId
    user = request.user.id
    phone = Phone.objects.get(id = productId)
    # creates or retrieves a wishlist based on the user_id generated, the creation of the wishlist is for unauthenticated user to have something to fill in there
    wish, created = WishList.objects.get_or_create(user_id=user)
    # retrieves the items in the wishlist of the user based on the wish created or gotten and the phone
    wishItem, created = WishItem.objects.get_or_create(wish=wish, phone=phone)
    #  based on the action i.e the button the wishItem reacts
    if action == 'add':
        wishItem.quantity += 1

    elif action =='remove':
        wishItem.quantity -= 1

    wishItem.save()
    
    if action =='delete':
        wishItem.delete()

    if wishItem.quantity <= 0:
        wishItem.delete()
        
    return JsonResponse('Item was added', safe=False)


def PhoneDetailView(request, id):
    data = get_object_or_404(Phone, pk=id)
    reviews = data.reviews
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():

            # Create Comment object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.data = data
            # Save the comment to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    context = {"data":data,
               "reviews": reviews,
               "new_review": new_review,
               "review_form": review_form}
    return render(request, 'price_compare_app/productinfo.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'first_name', ['jackgriffo49@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "price_compare_app/contact.html", {'form':form})

def documentation(request):
    return render(request,'price_compare_app/documentation/documentation.html')

def documentation_features(request):
    return render(request,'price_compare_app/documentation/documentationf.html')

def documentation_sign_up(request):
    return render(request,'price_compare_app/documentation/documentationh.html')

def documentation_compare_prices(request):
    return render(request,'price_compare_app/documentation/documentationi.html')

def documentation_search(request):
    return render(request,'price_compare_app/documentation/documentations.html')

def error_404_view(request,exception):
    return render(request,'price_compare_app/404.html')

def error_500_view(request):
    data = {}
    return render(request,'price_compare_app/404.html', data)

def iphone13(request):
    return render(request, 'price_compare_app/charts_html/iphone13promaxprice.html')


def categories(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo

    }
        
    return render(request,'price_compare_app/categories/iphone_category.html',context)


def infinix_category(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo
    }
        
    return render(request,'price_compare_app/categories/infinix_category.html',context)


def samsung_category(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo

    }
        
    return render(request,'price_compare_app/categories/samsung_category.html',context)


def tecno_category(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo

    }
        
    return render(request,'price_compare_app/categories/tecno_category.html',context)


def xiaomi_category(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo

    }
        
    return render(request,'price_compare_app/categories/xiaomi_category.html',context)


def oppo_category(request):
    iphone=Phone.objects.filter(brand__name__icontains='iphone')
    infinix=Phone.objects.filter(brand__name__icontains='infinix')
    samsung=Phone.objects.filter(brand__name__icontains='samsung')
    tecno=Phone.objects.filter(brand__name__icontains='tecno')
    xiaomi=Phone.objects.filter(brand__name__icontains='xiaomi')
    oppo=Phone.objects.filter(brand__name__icontains='oppo')

    context = {
        'iphones':iphone,
        'infinixs':infinix,
        'samsungs':samsung,
        'tecnos':tecno,
        'xiaomis':xiaomi,
        'oppos':oppo

    }
        
    return render(request,'price_compare_app/categories/oppo_category.html',context)
