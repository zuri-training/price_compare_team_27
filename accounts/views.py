from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CreateUserForm


# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=CreateUserForm()
        if request.method == "POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)

                return redirect('login')

        context={'form':form}
        return render(request,'accounts/signup.html',context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method =="POST":
            user_name= request.POST.get('username')
            password= request.POST.get('password')

            user=authenticate(request,username=user_name,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,"Username Or Password Is Incorrect")

    context = {}
    
    return render(request,'accounts/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/')