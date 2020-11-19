from api import serializer
from api import models
from api import filters
from api.baseview import Baseview
from api.runview import Runview

# Create your views here.

class ModulerViewSet(Baseview):
    queryset = models.Modular.objects.all()
    serializer_class = serializer.ModulerSerializer
    filter_class = filters.ModulerFilter

class UserViewSet(Baseview):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer
    filter_class = filters.UserFilter


class EnvironmentalViewSet(Baseview):
    queryset = models.Environmental.objects.all()
    serializer_class = serializer.EnvironmentalSerializer
    filter_class = filters.EnvironmentalFilter

class NoticeViewSet(Baseview):
    queryset = models.Notice.objects.all()
    serializer_class = serializer.NoticeSerializer
    filter_class = filters.NoticeFilter

class ConfigViewSet(Baseview):
    queryset = models.Config.objects.all()
    serializer_class = serializer.ConfigSerializer
    filter_class = filters.ConfigFilter

class CursorViewSet(Baseview):
    queryset = models.Cursor.objects.all()
    serializer_class = serializer.CursorSerializer
    filter_class = filters.CursorFilter

class ApiViewSet(Baseview):
    queryset = models.Api.objects.all()
    serializer_class = serializer.ApiSerializer
    filter_class = filters.ApiFilter

class runViewSet(Runview):
    queryset = models.Run.objects.all()
    serializer_class = serializer.RunSerializer
    filter_class = filters.RunFilter

