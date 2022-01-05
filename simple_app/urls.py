"""simple_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from the_app import views as app_views

urlpatterns = [
    path('signup/', app_views.signup, name='app-signup'),
    path('signin/', app_views.signin, name='app-signin'),
    path('', app_views.home, name='app-home'),
    path('myprofile/', app_views.Profile, name='app-profile'),
    path('signout/', app_views.signout, name='app-signout'),
    path('admin/', admin.site.urls),
]
