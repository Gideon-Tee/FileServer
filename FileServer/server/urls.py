from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('document-upload', views.upload_document, name='upload'),
    path('download/<int:document_id>', views.download_file, name='download'),
    path('email-send/<int:document_id>', views.send_file_via_email, name='send-file'),

]