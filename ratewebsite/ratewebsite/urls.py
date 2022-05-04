"""ratewebsite URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
# from rateinfo.views import *
from django.views.generic import RedirectView, TemplateView

from .views import redirect_root_view
urlpatterns = [
    path('',
         RedirectView.as_view(
             pattern_name='index_urlpattern',
             permanent=False
         )),
    path('index/',
         TemplateView.as_view(
             template_name='rateinfo/index.html'),
         name='index_urlpattern',
         ),
    path('login/',
         LoginView.as_view(template_name='rateinfo/login.html'),
         name='login_urlpattern'
         ),
    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
         ),
    path('', redirect_root_view),
    path('admin/', admin.site.urls),
    path('', include('rateinfo.urls')),
    # path('restaurant/', restaurant_list_view),
    # path('holder/', holder_list_view),
    # path('type/', type_list_view),
    # path('place/', place_list_view),
]
