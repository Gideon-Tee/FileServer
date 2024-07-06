from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
# Create your views here.


def index(request):
    return HttpResponse('<h1>Home page</h1>')


def signup(request):
    form = SignUpForm()

    context = {'form': form}
    return render(request, 'signup.html', context)