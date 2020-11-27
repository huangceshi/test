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
