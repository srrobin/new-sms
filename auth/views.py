from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm,EditRegisterForms
#from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successful')
            return redirect('home')
        else:
            messages.success(request, 'Try again')
            return redirect('login')
    return render(request,'auth/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'Login your account')
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "create account done")
            return redirect('home')

    else:
        form = RegisterForm()
    context = {"form": form }
    return render(request, 'auth/register.html', context)


def update_register(request):
    if request.method == "POST":
        form = EditRegisterForms(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "update done")
            return redirect('home')

    else:
        form = EditRegisterForms(instance=request.user)
    context = {"form": form }
    return render(request, 'auth/update_register.html', context)


def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')

    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form }
    return render(request, 'auth/change_password.html', context)