import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from price_compare_app.form import ReviewForm
from price_compare_app.models import *

from .form import ReviewForm
from .models import Phone

# Create your views here.

def get_random_four():
    pass

def get_latest_four():
    pass

def home_page(request):
    all_samsung= Phone.objects.filter(brand__name__icontains='samsung')
    all_iphones= Phone.objects.filter(brand__name__icontains='iphone')
    all_huawei= Phone.objects.filter(brand__name__icontains='huawei')


    context={
        'iphones':all_iphones,
        'samsung':all_samsung,
        'huawei':all_huawei
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
    print('Action:', action)
    print('productId:', productId)
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
