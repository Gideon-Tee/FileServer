from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import auth
# Create your views here.


def index(request):
    return render(request, 'server/index.html')


def signup(request):
    form = SignUpForm()

    context = {'form': form}
    return render(request, 'server/signup.html', context)

def login(request):

    return render(request, 'server/login.html')

def logout(request):
    
    return redirect('index')
