from rest_framework.views import exception_handler
#错误码定制表

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        # response.data['desc'] = response.data
        # response.data['data'] = None    #可以存在
        # del response.data['detail']  # 删除detail字段

    return response
