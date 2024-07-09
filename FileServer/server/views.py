from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import DocumentUploadForm
from .models import Document
# Create your views here.


def index(request):
    documents = Document.objects.all()
    return render(request, 'server/index.html', {'documents': documents})


def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully')
            return redirect('index')

    else:
        form = DocumentUploadForm()
    return render(request, 'server/upload-document.html', {'form': form})


def signup(request):
    form = SignUpForm()

    context = {'form': form}
    return render(request, 'account/signup.html', context)

def login(request):

    return render(request, 'account/login.html')

def logout(request):
    
    return redirect('index')
