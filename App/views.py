from django.shortcuts import render,HttpResponse

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CourtEvent, Advocate, Case
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Home and Base Views
def home(request):
    return render(request, 'Home.html')


def base_view(request):
    return render(request, 'base.html')


# Portfolio View
def portfolio(request):
    return render(request, 'portfolio.html')




# Court Calendar View
def court_calendar(request):
    events = CourtEvent.objects.all().order_by('date', 'time')
    return render(request, 'calendar/court_calendar.html', {'events': events})


# Team View
def team(request):
    users = CustomUser.objects.all()
    advocates = Advocate.objects.all()


# User Views
def custom_user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'custom_user_list.html', {'users': users})


def custom_user_detail(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'custom_user_detail.html', {'user': user})

    return render(request, 'advocate_detail.html', context)




# Client View
def client_view(request):
    return render(request, 'client.html')


# Clerk View
def clerk_view(request):
    return render(request, 'clerk.html')


# About View
def about(request):
    return render(request,'about.html')

def Advocate_Signup(request):
    return render(request,'advocate.html')



def advocate_view(request):
    if request.method == 'POST':
        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = Fname
        myuser.last_name = Lname
        myuser.save

        messages.success(request, "account created succesfully")
        return redirect('login')

def advocate_login(request):
    return render(request,'advocatelogin.html')



# Logout View
def user_logout(request):
    logout(request)
    return redirect('home')



    