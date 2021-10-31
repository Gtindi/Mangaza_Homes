"""mangaza URL Configuration

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
from django.urls import path
from . import views
# new
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',views.test, name="test"),
    path('',views.home, name="home"),
    path('team0/', views.about, name='team0'),
    path('blog/', views.blog, name="blog"),
    path('booking/', views.booking, name="booking"),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name="feature"),
    path('menu/', views.menu, name="menu"),
    path('single/', views.single, name="single"),
    path('team/', views.team, name="team"),
    path('vacation/', views.team0, name="vacation"),
    path('kings/', views.kings, name="kings"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)