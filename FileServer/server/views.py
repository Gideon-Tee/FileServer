from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse, Http404
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .forms import DocumentUploadForm, CustomSignUpForm, EmailSendForm
from .models import Document
from django.db.models import Q 
# Create your views here.

@login_required(login_url='account_login')
def index(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    username = get_username(request.user.email)
    documents = Document.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q)
    )
    context = {
        'documents': documents,
        'username': username
    }
    return render(request, 'server/index.html', context)

# Generate a username for the user using their email
def get_username(email_address):
    username = ''
    for ch in email_address:
        if ch == '@':
            break
        username += ch
    return username


@login_required(login_url='account_login')
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully')
            return redirect('index')

    else:
        form = DocumentUploadForm()
    
    context = {
        'form': form,
        'username': get_username(request.user.email)
    }
    return render(request, 'server/upload-document.html', context)

@login_required(login_url='account_login')
def send_file_via_email(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']

            # Create the email
            email = EmailMessage(
                subject=f"Document: {document.title}",
                body="Please find the attached document, from Lizzy's FileServer.",
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
    context = {
        'form': form,
        'document': document,
        'username': get_username(request.user.email)
    }
    return render(request, 'server/send-mail.html', context)

@login_required(login_url='account_login')
def download_file(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    file_path = document.file.path

    try:
        document.downloads += 1
        document.save()
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=document.file.name)
    except FileNotFoundError:
        raise Http404("File does not exist")


login_required(login_url='account_login')
def logout(request):
    auth.logout(request)
    return redirect('index')
