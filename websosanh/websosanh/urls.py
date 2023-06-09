"""websosanh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
# from main.views import GetAllProductAPIView
from main.views import prod,home,register
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/product/',GetAllProductAPIView.as_view()),
    path('main/',prod),
    path('',home),
    path('main/register/',register),
    path('accounts/', include('allauth.urls'))
]
# handler404 = 'main.views.handler404'
# handler500 = 'main.views.handler500'