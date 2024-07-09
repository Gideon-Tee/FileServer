from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse, Http404
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import DocumentUploadForm, SignUpForm, EmailSendForm
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


def send_file_via_email(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']

            # Create the email
            email = EmailMessage(
                subject=f"Document: {document.title}",
                body="Please find the attached document.",
                to=[recipient_email],
            )

            # Attach the file
            email.attach_file(document.file.path)

            # Send the email
            email.send()
            document.emails_sent += 1
            document.save()
            messages.success(request, 'Email sent successfully')
            return redirect('index')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('send-file')
    
    form = EmailSendForm()

    return render(request, 'server/send-mail.html', {'form': form, 'document': document})


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
