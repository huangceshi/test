"""testPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from api import views
router = routers.DefaultRouter()
router.register('moduler',viewset=views.ModulerViewSet)
router.register('user',viewset=views.UserViewSet)
router.register('environmental',viewset=views.EnvironmentalViewSet)
router.register('notice',viewset=views.NoticeViewSet)
router.register('config',viewset=views.ConfigViewSet)
router.register('cursor',viewset=views.CursorViewSet)
router.register('api',viewset=views.ApiViewSet)
router.register('run',viewset=views.runViewSet)



urlpatterns = [
    path('api/',include(router.urls)),
]
