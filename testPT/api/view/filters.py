import django_filters
from api import models


class ModulerFilter(django_filters.rest_framework.FilterSet):
    platform = django_filters.rest_framework.CharFilter(field_name='platform', lookup_expr='icontains')
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    moduless = django_filters.rest_framework.CharFilter(field_name='moduless', lookup_expr='icontains')
    class Meta:
        model = models.Modular
        fields = ['platform','id','moduless']



class UserFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    email = django_filters.rest_framework.CharFilter(field_name='email', lookup_expr='exact')
    password = django_filters.rest_framework.CharFilter(field_name='password', lookup_expr='exact')
    username = django_filters.rest_framework.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = models.User
        fields = ['id','email','username']

class EnvironmentalFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    class Meta:
        model = models.Environmental
        fields = ['id']

class NoticeFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    user_id = django_filters.rest_framework.CharFilter(field_name='user_id', lookup_expr='icontains')
    class Meta:
        model = models.Notice
        fields = ['id','user_id']


class ConfigFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    key = django_filters.rest_framework.CharFilter(field_name='key', lookup_expr='icontains')
    class Meta:
        model = models.Config
        fields = ['id','key']

class CursorFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    run_id = django_filters.rest_framework.CharFilter(field_name='run_id', lookup_expr='icontains')
    api_id = django_filters.rest_framework.CharFilter(field_name='api_id', lookup_expr='icontains')
    usr_key = django_filters.rest_framework.CharFilter(field_name='usr_key', lookup_expr='icontains')
    class Meta:
        model = models.Cursor
        fields = ['id','api_id','run_id','usr_key']

class ApiFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    modular = django_filters.rest_framework.NumberFilter(field_name='modular_id')
    casename = django_filters.rest_framework.CharFilter(field_name='casename', lookup_expr='icontains')

    class Meta:
        model = models.Api
        fields = ['id','modular','casename']

class RunFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='icontains')
    modular_id = django_filters.rest_framework.CharFilter(field_name='modular_id', lookup_expr='icontains')
    user_id = django_filters.rest_framework.CharFilter(field_name='user_id', lookup_expr='icontains')
    api_id = django_filters.rest_framework.CharFilter(field_name='api_id', lookup_expr='icontains')

    class Meta:
        model = models.Run
        fields = ['id','modular_id','user_id','api_id']
