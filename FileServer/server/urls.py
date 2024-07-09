from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('document-upload', views.upload_document, name='upload'),
    path('download/<int:document_id>', views.download_file, name='download'),

]