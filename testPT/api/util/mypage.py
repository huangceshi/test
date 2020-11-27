from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    default_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 30
