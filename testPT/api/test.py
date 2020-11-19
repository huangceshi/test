import requests
from requests.packages import urllib3
import jsonpath
import json
# import jsonpath
# port json
# import os
import time
import json
# #忽略关闭ssl的安全警告
urllib3.disable_warnings()
import pytest
import allure



#请求数据得转换
# url ='https://oapi-smix1.t.blingabc.com/auth/open-api/foreign/useradmin/v1/login'
# data ={"userName":"crmadmin","password":"bling123"}
# header = {'Content-Type':'application/json;charset=UTF-8'}
# r = requests.post(url=url, json=data,headers=header,verify=False)
# print(r.status_code)
# a =r.text
# print(a)
# a = str(a)
# print(a)
# print(type(a))
# a =json.loads(a)
# print(a)
# print(type(a))
#
# res =jsonpath.jsonpath(a,'$..token')
# print(res[0])
#
# aa =jsonpath.jsonpath(a,'$.data.userInfoVO.[1].id')
# print(aa[0])
#
# aaa =

# a ='abcedfg'
# print(a[0:3])
# print(a[3:])










#get请求
# url2='https://fapi-smix1.t.blingabc.com/fts/user-api/talk/v1/app-foreignlist?adminId=20'
# header = {'Content-Type':'application/json;charset=UTF-8','token':'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb20ueGRmLmJsaW5nIiwiYXVkIjoiY2xpZW50IiwidXNlcmNvZGUiOiJjcm1hZG1pbiIsImV4cCI6MTYwNTY4NjU1NCwiaWF0IjoxNjA1MDgxNzU0fQ.gIKAHOqnGGloEMDgEJ4l066PWhAaNd3iwL6rTELV88b2yqO19T5rbtWNJQ3fxPlSZV_crHd8wtrx4uSXu2l8Ew'}
# r = requests.get(url =url2,headers=header,verify=False)
# print(r.text)
# a =round(r.elapsed.total_seconds()*1000)
# print(a)

#post请求
# url3 = 'https://oapi-smix1.t.blingabc.com/tutor/user-api/dingtalk/v2/msglist'
# header ={'Content-Type':'application/json;charset=UTF-8','token':'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb20ueGRmLmJsaW5nIiwiYXVkIjoiY2xpZW50IiwidXNlcmNvZGUiOiJjcm1hZG1pbiIsImV4cCI6MTYwNTY4NjU1NCwiaWF0IjoxNjA1MDgxNzU0fQ.gIKAHOqnGGloEMDgEJ4l066PWhAaNd3iwL6rTELV88b2yqO19T5rbtWNJQ3fxPlSZV_crHd8wtrx4uSXu2l8Ew'}
# # data ={"page":1,"size":20,"teacherId":20,"readed":0}
# data ={'page':1,'size':20,'teacherId':20,'readed':0}
# r= requests.post(url=url3,headers=header,verify=False,json=data)
# print(r.text)

#图片上传
# url='https://oapi-smix1.t.blingabc.com/foreign/admin-api/file/v1/oss/upload/publicRead'
# headers ={'Content-Disposition': 'form-data', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.11.0', 'Connection': 'keep-alive'}
# files = {'file':('png.png','open(".api/data/upload/png.png", "rb")')}
# r = requests.request(headers=headers,method='POST',url=url,files=files,verify=False, timeout=5)
# print(r.text)


# a ={"userName":"crmadmin","password":"bling123"}
# # print(type(a))
# # a =str(a)
# # print(a)
# # print(type(a))
# # a =json.loads(a)
# # print(a)
# # print(type(a))
# # a =json.loads(a)
# # print(a)
# # print(type(a))

# print(a.keys())
# for i in a.keys():
#     print(i)
#
# a['2']=3
# print(a)


# a ={'userName': 'crmadmin', 'password': 'bling123'}
# print(type(a))
#
# a =json.loads(json.dumps(a))
# print(a)
# print(type(a))

# a ={'userName': 'crmadmin', 'password': 'bling123'}
# for i in a.keys():
#     print(i)
#     b ='$..'+i
#     key = jsonpath.jsonpath(a, '$..'+i)
#     # key = jsonpath.jsonpath(a, '$..userName')
#     print(key[0])

# print(time.time())
# print(time.asctime( time.localtime(time.time()) ))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )


# name='png.png'
# file_address ={'file': ('1', 'open(".api/data/upload/1", "rb")')}
# print(file_address['file'])
# print(type(file_address['file']))
# a =file_address['file']
#
# value = str(file_address['file'])
# print(value)
# print(type(value))
# value=value.replace("1",name)
# print(value)
# value=tuple(value)
# print(111)
# print(value)
# print(type(value))
# file_address['file']=value
# print(file_address)

#
# name='png.png'
# file_address ={'file': ('1', 'open(".api/data/upload/1", "rb")')}
# print(type(file_address))
#
# a =json.dumps(file_address)
# print(a)
# print(type(a))
# a =a.replace("1",name)
# print(a)
# print(type(a))
# a =json.loads(a)
# print(a)
# print(type(a))

#
# pytest.main(['--alluredir','./data/html/'])
#
#
# # a =12344
# # a =str(a)
# # print(len(a))
# @allure.feature('加入购物车')
# def test_1():
#     assert 1 == 1
# test_1()
# a ='bbc'
# a =str(a)
# print(a)
# print(len(a))

# a =1
# import os
# os.system('allure')

# a =['a','v']
# print(len(a))

# a ={"code":10000,"msg":"操作成功","data":{"userInfoVO":{"id":20,"teacherId":None,"teacherCode":None,"username":"crmadmin","createDate":None,"lastLoginDate":"2020-11-18 10:00:14","lastLoginIp":"172.17.71.154","name":"crmadmin","email":"dengnan6@xdf.cn","phone":"13910797177","headImg":None,"status":1,"delStatus":0,"token":"eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb20ueGRmLmJsaW5nIiwiYXVkIjoiY2xpZW50IiwidXNlcmNvZGUiOiJjcm1hZG1pbiIsImV4cCI6MTYwNjI2OTYxNCwiaWF0IjoxNjA1NjY0ODE0fQ.J7QC_Dm2XleGStG6uff2kqNxr3AcNj1g07kQF5b1TNA2wH6ul9JIrk8sM3cCpFtUHSu8aajT8cWsqiGyD1r3fA","roleType":None,"userType":None,"wechatCode":None,"wechatImageUrl":None,"groupType":None,"roleId":"105,81,92,96,111,112,104","channelCodes":None,"organizationId":72,"roleList":[{"id":81,"name":"外教新平台超级管理员","valid":1,"type":10,"platformCode":"0002","description":"","delStatus":0,"creator":None,"createDate":"2019-04-08 14:42:09","updateDate":"2019-07-30 15:18:31"},{"id":92,"name":"外教平台超级管理员","valid":1,"type":10,"platformCode":"0002","description":"","delStatus":0,"creator":None,"createDate":"2019-08-01 19:31:31","updateDate":"2019-08-01 20:03:13"},{"id":96,"name":"管理部管理员","valid":1,"type":10,"platformCode":"0002","description":"管理部管理员","delStatus":0,"creator":None,"createDate":"2019-10-23 15:33:47","updateDate":"2019-10-23 15:33:47"}],"menuActions":None},"dingTalkBindStatus":None,"salerInfo":None}}
#
#
# aa =jsonpath.jsonpath(a,'$.data.userInfoVO.roleList.[1].id')
# print(aa[0])


# 发送带有附件的邮件。
# c ='C:\Users\bling\PycharmProjects\testPT\api'
# a =r'c'
# a =a.replace("\\","/")
# print(a)

# import os
# b = os.getcwd()[:-4]
# print(b)
# c = r"/".join(b.split("\\"))
# print (c)        #获取到的形式就为：D://Auto//test//mobule

# str1 = '123  456  7\t8\r9\n10'
# str1 = re.sub('[\s+]', '', str1)
# print(str1)


# a ='abc'
# a =a.replace('a','b')
# print(a)

a ='a\nbc'
print(a)