from rest_framework import viewsets,status
from rest_framework.response import Response
import django_filters
from api.util.util import Util
import jsonpath
class Runview(viewsets.ModelViewSet):

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    #增加
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 重写数据返回格式
        data = {'status_code': status.HTTP_200_OK, 'data': serializer.data}

        returndata = Util.ApiSelect(data)
        id = jsonpath.jsonpath(data, '$..id')[0]
        Util.nowrun(returndata['key'],id)
        requestdata = Util.getrequest(data)
        data = {'status_code': status.HTTP_200_OK, 'data': requestdata}
        return Response(data=data, status=status.HTTP_201_CREATED, headers=headers)

    #多个查询
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        data = {'status_code': status.HTTP_200_OK,
                'data': {
                    'count': len(serializer.data),
                    'posts': serializer.data}}

        return Response(data)
    #单个查询
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        data = {'status_code': status.HTTP_200_OK, 'data': serializer.data}
        return Response(data)
