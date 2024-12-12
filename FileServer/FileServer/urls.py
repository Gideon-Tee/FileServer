"""
URL configuration for FileServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
# import allauth.account.views as allauth_views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('server.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/login', allauth_views.login, name='account_login'),
    # path('accounts/signup', allauth_views.signup, name='account_signup'),
    # path('accounts/logout', allauth_views.logout, name='account_logout'),
    # path('accounts/confirm-email/', allauth_views.email_verification_sent, name='account_email_verification_sent'),
    # path('accounts/confirm-email/<str:key>/', allauth_views.confirm_email, name='account_confirm_email'),
    # path('accounts/password/reset/', allauth_views.password_reset, name='account_reset_password'),
    # path('accounts/password/reset/done/', allauth_views.password_reset_done, name='account_reset_password_done'),
    # path('accounts/password/reset/key/done/', allauth_views.password_reset_from_key_done, name='account_reset_password_from_key_done'),
    # path('accounts/password/reset/key/<uidb64>/<token>/', allauth_views.password_reset_from_key, name='account_reset_password_from_key'),
]

handler404 = 'django.views.defaults.page_not_found'
