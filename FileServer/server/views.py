from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, Http404
from .forms import SignUpForm
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import DocumentUploadForm
from .models import Document
from django.db.models import Q 
# Create your views here.


def index(request):
    q = request.GET.get('q') if request.GET.get('q') else ''

    documents = Document.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q)
    )
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


def download_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = document.file.path

    try:
        document.downloads += 1
        document.save()
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=document.file.name)
    except FileNotFoundError:
        raise Http404("File does not exist")

def signup(request):
    form = SignUpForm()

    context = {'form': form}
    return render(request, 'account/signup.html', context)

def login(request):

    return render(request, 'account/login.html')

def logout(request):
    
    return redirect('index')
