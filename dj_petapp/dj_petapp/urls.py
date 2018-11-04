"""dj_petapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # url(r'^$', views.index,name='myindex'),
    url(r'^adopt/', include('adopt.urls', namespace='dj_petapp.adopt')),
    url(r'^user/', include('user.urls', namespace='dj_petapp.user')),
    url(r'^lingyang/', include('lingyang.urls', namespace='dj_petapp.lingyang')),
    url(r'^forum/', include('forum.urls', namespace='dj_petapp.forum')),
    url(r'^petshow/', include('petshow.urls', namespace='dj_petapp.petshow')),
    url(r'personal/', include("personal.urls", namespace="personal")),
]
