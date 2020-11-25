from api import serializer
from api import models
from api import filters
from api.baseview import Baseview
from api.runview import Runview
from rest_framework.decorators import action
import json
from rest_framework.response import Response
from rest_framework import status


class ModulerViewSet(Baseview):
    queryset = models.Modular.objects.all()
    serializer_class = serializer.ModulerSerializer

    @action(methods=['get'], detail=False)
    def all(self, request):
        list = [{'基础业务线': 1}, {'外教业务线': 2}, {'用户端业务线': 3}, {'教学业务线': 4}, {'增长业务线': 5}, {'活动课件': 6}, {'课程顾问': 7},
                {'备用业务线1': 8},
                {'备用业务线2': 9}]
        modulerlist=[]
        for platformname in list:

            for key in platformname:
                valuedata =platformname[key]
                valuelist = {'id': '', 'platformname': '', 'lists': ''}
                key1 = models.Modular.objects.filter(platform=key)
                value = serializer.ModulerSerializer(key1, many=True).data
                del value[0]
                if len(value) >0:
                    list=[]
                    for i in value:
                        i = json.loads(json.dumps(i))
                        list.append(i)
                    valuelist['lists'] = list
                    valuelist['id'] = valuedata
                    valuelist['platformname'] = key
                else:
                    pass
            modulerlist.append(valuelist)
        return Response(data={'code': status.HTTP_200_OK,  'data': modulerlist})

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



