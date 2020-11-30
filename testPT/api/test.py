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

# a = '1,2,3'
# a = a.split(',')
# print(a)
# print(type(a))
# a =[{"key":"token"}]
# print(type(a))
# print(a[0])
# a =str(a)
# b =list(a)
# print(type(b))
# print(b)
# print(b[0])

# import json
# a=["1","2","3"]
# a =str(a)
# b=json.loads(a)
# print(b)

# a =[{"key":"token"}]
# a =str(a)
# b =a.split()
# print(b)
# print(type(b))
# print(len(b))

# a =[{"key":"token"},{"key":"哈哈哈"}]
# a =str(a)
# b =a.split()
# print(b)
# print(type(b))
# print(len(b))

# a = [{"key":"token"},{"key":"哈哈哈"}]
# a =str(a)
# b = json.dumps(a)
# print (b)
# print (type(b))
# c=json.loads(b)
#
# print (c)
# print(type(c))
# print(len(c))

a ={"code":10000,"msg":"操作成功","data":{"userInfoVO":{"id":20,"teacherId":"","teacherCode":"","username":"crmadmin","createDate":"","lastLoginDate":"2020-11-30 16:00:30","lastLoginIp":"172.17.71.154","name":"crmadmin","email":"dengnan6@xdf.cn","phone":"13910797177","headImg":"","status":1,"delStatus":0,"token":"eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb20ueGRmLmJsaW5nIiwiYXVkIjoiY2xpZW50IiwidXNlcmNvZGUiOiJjcm1hZG1pbiIsImV4cCI6MTYwNzMyODAzMCwiaWF0IjoxNjA2NzIzMjMwfQ.3mbKpo6lOLKWrFW6xt3xghB9iDkzdSm1sX05xpt1N-KynOgAnSJtod0YzChNOU8trorGy97m4SZnBpUcjIMACA","roleType":"","userType":"","wechatCode":"","wechatImageUrl":"","groupType":"","roleId":"105,81,92,96,111,112,104","channelCodes":"","organizationId":72,"roleList":[{"id":81,"name":"外教新平台超级管理员","valid":1,"type":10,"platformCode":"0002","description":"","delStatus":0,"creator":"","createDate":"2019-04-08 14:42:09","updateDate":"2019-07-30 15:18:31"},{"id":92,"name":"外教平台超级管理员","valid":1,"type":10,"platformCode":"0002","description":"","delStatus":0,"creator":"","createDate":"2019-08-01 19:31:31","updateDate":"2019-08-01 20:03:13"},{"id":96,"name":"管理部管理员","valid":1,"type":10,"platformCode":"0002","description":"管理部管理员","delStatus":0,"creator":"","createDate":"2019-10-23 15:33:47","updateDate":"2019-10-23 15:33:47"},{"id":104,"name":"crmadmin","valid":1,"type":10,"platformCode":"0004","description":"","delStatus":0,"creator":"","createDate":"2020-07-08 11:16:46","updateDate":"2020-07-08 11:24:09"},{"id":105,"name":"crmadmin","valid":1,"type":10,"platformCode":"0007","description":"","delStatus":0,"creator":"","createDate":"2020-07-08 14:48:04","updateDate":"2020-08-27 14:16:53"},{"id":111,"name":"入职合同终审角色","valid":1,"type":10,"platformCode":"0002","description":"入职合同终审按钮权限","delStatus":0,"creator":"","createDate":"2020-08-04 10:23:51","updateDate":"2020-08-04 10:23:51"},{"id":112,"name":"招聘主管","valid":1,"type":10,"platformCode":"0002","description":"","delStatus":0,"creator":"","createDate":"2020-08-19 10:17:45","updateDate":"2020-08-19 10:17:45"}],"authorization":"","expirationDate":"","dingTalkUnionId":""},"menuList":[{"id":152,"cnName":"首页","platformCode":"0002","parentId":0,"level":1,"url":"entrance","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":181,"cnName":"监课管理","platformCode":"0002","parentId":0,"level":1,"url":"monitor","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":254,"cnName":"监课平台","platformCode":"0002","parentId":0,"level":1,"url":"monitor-platform","icon":"monitor-platform","sort":1,"childMenus":"","menuActions":""},{"id":257,"cnName":"工单","platformCode":"0002","parentId":0,"level":1,"url":"work-order","icon":"work-order","sort":2,"childMenus":[{"id":258,"cnName":"我提交的","platformCode":"0002","parentId":257,"level":2,"url":"create","icon":"create","sort":1,"childMenus":"","menuActions":""},{"id":259,"cnName":"我处理的","platformCode":"0002","parentId":257,"level":2,"url":"deal","icon":"deal","sort":2,"childMenus":"","menuActions":""},{"id":260,"cnName":"所有工单","platformCode":"0002","parentId":257,"level":2,"url":"all","icon":"all","sort":3,"childMenus":"","menuActions":""}],"menuActions":""},{"id":267,"cnName":"账号速查","platformCode":"0002","parentId":0,"level":1,"url":"monitor-platform/account-quick","icon":"account-quick","sort":3,"childMenus":"","menuActions":""},{"id":205,"cnName":"招聘管理","platformCode":"0002","parentId":0,"level":1,"url":"recruitment","icon":"","sort":3,"childMenus":[{"id":206,"cnName":"招聘数据统计","platformCode":"0002","parentId":205,"level":2,"url":"statistics","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":207,"cnName":"注册未填信息用户","platformCode":"0002","parentId":205,"level":2,"url":"register","icon":"aaa","sort":2,"childMenus":"","menuActions":""},{"id":208,"cnName":"简历管理","platformCode":"0002","parentId":205,"level":2,"url":"resume","icon":"","sort":3,"childMenus":"","menuActions":""},{"id":209,"cnName":"面试管理","platformCode":"0002","parentId":205,"level":2,"url":"interview","icon":"","sort":4,"childMenus":"","menuActions":""},{"id":210,"cnName":"资质管理","platformCode":"0002","parentId":205,"level":2,"url":"trial","icon":"","sort":5,"childMenus":"","menuActions":""},{"id":212,"cnName":"入职管理","platformCode":"0002","parentId":205,"level":2,"url":"entry","icon":"","sort":6,"childMenus":"","menuActions":""},{"id":213,"cnName":"合同管理","platformCode":"0002","parentId":205,"level":2,"url":"contract","icon":"","sort":7,"childMenus":"","menuActions":""},{"id":275,"cnName":"渠道管理","platformCode":"0002","parentId":205,"level":2,"url":"channel","icon":"channel","sort":8,"childMenus":"","menuActions":""},{"id":306,"cnName":"招聘黑名单","platformCode":"0002","parentId":205,"level":2,"url":"blacklist","icon":"","sort":8,"childMenus":"","menuActions":""}],"menuActions":""},{"id":268,"cnName":"培训管理","platformCode":"0002","parentId":0,"level":1,"url":"training","icon":"training","sort":4,"childMenus":[{"id":269,"cnName":"培训项目管理","platformCode":"0002","parentId":268,"level":2,"url":"project","icon":"project","sort":1,"childMenus":"","menuActions":""},{"id":273,"cnName":"培训标签","platformCode":"0002","parentId":268,"level":2,"url":"tag","icon":"tag","sort":2,"childMenus":"","menuActions":""},{"id":270,"cnName":"入职培训管理","platformCode":"0002","parentId":268,"level":2,"url":"orientation","icon":"orientation","sort":3,"childMenus":"","menuActions":""},{"id":271,"cnName":"上岗培训管理","platformCode":"0002","parentId":268,"level":2,"url":"mount-guard","icon":"mount-guard","sort":4,"childMenus":"","menuActions":""},{"id":272,"cnName":"磨课管理","platformCode":"0002","parentId":268,"level":2,"url":"mock","icon":"mock","sort":5,"childMenus":"","menuActions":""},{"id":280,"cnName":"在职培训管理","platformCode":"0002","parentId":268,"level":2,"url":"on-job","icon":"on-job","sort":5,"childMenus":"","menuActions":""},{"id":274,"cnName":"我的任务及管理","platformCode":"0002","parentId":268,"level":2,"url":"task-manage","icon":"task-manage","sort":7,"childMenus":"","menuActions":""},{"id":305,"cnName":"外教评语","platformCode":"0002","parentId":268,"level":2,"url":"comments","icon":"","sort":8,"childMenus":"","menuActions":""}],"menuActions":""},{"id":291,"cnName":"审批管理","platformCode":"0002","parentId":0,"level":1,"url":"approval","icon":"approval","sort":4,"childMenus":[{"id":292,"cnName":"审批项目","platformCode":"0002","parentId":291,"level":2,"url":"approval-project","icon":"approval-project","sort":1,"childMenus":"","menuActions":""},{"id":296,"cnName":"审批任务","platformCode":"0002","parentId":291,"level":2,"url":"approval-task","icon":"approval-task","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":307,"cnName":"邮件管理","platformCode":"0002","parentId":0,"level":1,"url":"mail","icon":"mail","sort":5,"childMenus":[{"id":308,"cnName":"邮件列表","platformCode":"0002","parentId":307,"level":2,"url":"mail-list","icon":"","sort":1,"childMenus":"","menuActions":""}],"menuActions":""},{"id":217,"cnName":"外教管理","platformCode":"0002","parentId":0,"level":1,"url":"foreign-teacher","icon":"","sort":5,"childMenus":"","menuActions":""},{"id":248,"cnName":"消息管理","platformCode":"0002","parentId":0,"level":1,"url":"message","icon":"message","sort":5,"childMenus":[{"id":249,"cnName":"新建消息","platformCode":"0002","parentId":248,"level":2,"url":"new-message","icon":"new-message","sort":1,"childMenus":"","menuActions":""},{"id":250,"cnName":"草稿箱","platformCode":"0002","parentId":248,"level":2,"url":"draft-box","icon":"draft-box","sort":2,"childMenus":"","menuActions":""},{"id":278,"cnName":"消息一审","platformCode":"0002","parentId":248,"level":2,"url":"trial-first","icon":"trial-first","sort":3,"childMenus":"","menuActions":""},{"id":279,"cnName":"消息二审","platformCode":"0002","parentId":248,"level":2,"url":"trial-second","icon":"trial-second","sort":4,"childMenus":"","menuActions":""},{"id":251,"cnName":"已发送","platformCode":"0002","parentId":248,"level":2,"url":"already-send","icon":"already-send","sort":5,"childMenus":"","menuActions":""},{"id":252,"cnName":"消息类型","platformCode":"0002","parentId":248,"level":2,"url":"message-type","icon":"message-type","sort":6,"childMenus":"","menuActions":""},{"id":253,"cnName":"文件上传","platformCode":"0002","parentId":248,"level":2,"url":"file-upload","icon":"file-upload","sort":7,"childMenus":"","menuActions":""}],"menuActions":""},{"id":298,"cnName":"外教设备变更管理","platformCode":"0002","parentId":0,"level":1,"url":"device","icon":"","sort":7,"childMenus":[{"id":299,"cnName":"外教设备变更","platformCode":"0002","parentId":298,"level":2,"url":"device-change","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":300,"cnName":"设备列表","platformCode":"0002","parentId":298,"level":2,"url":"device-list","icon":"","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":223,"cnName":"班级管理","platformCode":"0002","parentId":0,"level":1,"url":"class","icon":"class","sort":7,"childMenus":[{"id":238,"cnName":"班级列表","platformCode":"0002","parentId":223,"level":2,"url":"class-list","icon":"class-list","sort":1,"childMenus":"","menuActions":""},{"id":239,"cnName":"任务列表","platformCode":"0002","parentId":223,"level":2,"url":"task-list","icon":"task-list","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":255,"cnName":"标签管理","platformCode":"0002","parentId":0,"level":1,"url":"tag","icon":"tag","sort":7,"childMenus":"","menuActions":""},{"id":311,"cnName":"督课","platformCode":"0002","parentId":0,"level":1,"url":"supervisor","icon":"","sort":8,"childMenus":[{"id":313,"cnName":"督课","platformCode":"0002","parentId":311,"level":2,"url":"supervisor","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":315,"cnName":"数据统计","platformCode":"0002","parentId":311,"level":2,"url":"statistic","icon":"","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":241,"cnName":"抢课管理","platformCode":"0002","parentId":0,"level":1,"url":"grab-course","icon":"grab-course","sort":8,"childMenus":[{"id":242,"cnName":"抢课任务","platformCode":"0002","parentId":241,"level":2,"url":"task-list","icon":"task-list","sort":1,"childMenus":"","menuActions":""}],"menuActions":""},{"id":312,"cnName":"投诉","platformCode":"0002","parentId":0,"level":1,"url":"complaint","icon":"","sort":9,"childMenus":[{"id":316,"cnName":"投诉","platformCode":"0002","parentId":312,"level":2,"url":"complaint","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":317,"cnName":"数据统计","platformCode":"0002","parentId":312,"level":2,"url":"statistic","icon":"","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":179,"cnName":"课程管理","platformCode":"0002","parentId":0,"level":1,"url":"course","icon":"","sort":9,"childMenus":"","menuActions":""},{"id":276,"cnName":"操作日志","platformCode":"0002","parentId":0,"level":1,"url":"log","icon":"log","sort":10,"childMenus":"","menuActions":""},{"id":224,"cnName":"监课管理","platformCode":"0002","parentId":0,"level":1,"url":"monitor-class","icon":"monitor-class","sort":11,"childMenus":[{"id":297,"cnName":"监课记录","platformCode":"0002","parentId":224,"level":2,"url":"log","icon":"log","sort":1,"childMenus":"","menuActions":""},{"id":225,"cnName":"未开始监课","platformCode":"0002","parentId":224,"level":2,"url":"wait","icon":"wait-monitor","sort":1,"childMenus":"","menuActions":""},{"id":233,"cnName":"待详查监课","platformCode":"0002","parentId":224,"level":2,"url":"survey","icon":"survey","sort":2,"childMenus":"","menuActions":""},{"id":234,"cnName":"需改进监课","platformCode":"0002","parentId":224,"level":2,"url":"improve","icon":"improve","sort":3,"childMenus":"","menuActions":""},{"id":235,"cnName":"未达标监课","platformCode":"0002","parentId":224,"level":2,"url":"unqualified","icon":"unqualified","sort":4,"childMenus":"","menuActions":""},{"id":236,"cnName":"已达标监课","platformCode":"0002","parentId":224,"level":2,"url":"finished","icon":"finished","sort":5,"childMenus":"","menuActions":""},{"id":237,"cnName":"已作废监课","platformCode":"0002","parentId":224,"level":2,"url":"invalid","icon":"invalid","sort":6,"childMenus":"","menuActions":""},{"id":231,"cnName":"监课数据统计","platformCode":"0002","parentId":224,"level":2,"url":"monitor-count","icon":"monitor-count","sort":7,"childMenus":"","menuActions":""},{"id":318,"cnName":"督导名单","platformCode":"0002","parentId":224,"level":2,"url":"supervisor","icon":"","sort":10,"childMenus":"","menuActions":""}],"menuActions":""},{"id":226,"cnName":"评估课程管理","platformCode":"0002","parentId":0,"level":1,"url":"course-evaluation","icon":"course-evaluation","sort":13,"childMenus":[{"id":227,"cnName":"未评估课程","platformCode":"0002","parentId":226,"level":2,"url":"not","icon":"not","sort":1,"childMenus":"","menuActions":""},{"id":228,"cnName":"已评估课程","platformCode":"0002","parentId":226,"level":2,"url":"already","icon":"already","sort":2,"childMenus":"","menuActions":""},{"id":229,"cnName":"评估数据统计","platformCode":"0002","parentId":226,"level":2,"url":"statistics","icon":"statistics","sort":3,"childMenus":"","menuActions":""},{"id":230,"cnName":"月评估外教","platformCode":"0002","parentId":226,"level":2,"url":"foreign-list","icon":"foreign-list","sort":4,"childMenus":"","menuActions":""}],"menuActions":""},{"id":182,"cnName":"智能排班管理","platformCode":"0002","parentId":0,"level":1,"url":"scheduling","icon":"","sort":15,"childMenus":[{"id":189,"cnName":"排班属性配置","platformCode":"0002","parentId":182,"level":2,"url":"property","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":218,"cnName":"可用时间预览","platformCode":"0002","parentId":182,"level":2,"url":"available-time","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":219,"cnName":"同步开放时间","platformCode":"0002","parentId":182,"level":2,"url":"open-time","icon":"","sort":3,"childMenus":"","menuActions":""},{"id":256,"cnName":"外教分类","platformCode":"0002","parentId":182,"level":2,"url":"foreign-sort","icon":"foreign-sort","sort":5,"childMenus":"","menuActions":""}],"menuActions":""},{"id":180,"cnName":"外教日常管理","platformCode":"0002","parentId":0,"level":1,"url":"daily","icon":"","sort":17,"childMenus":[{"id":190,"cnName":"请假管理","platformCode":"0002","parentId":180,"level":2,"url":"leave","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":266,"cnName":"请假统计","platformCode":"0002","parentId":180,"level":2,"url":"leave-statistics","icon":"leave-statistics","sort":2,"childMenus":"","menuActions":""},{"id":191,"cnName":"签到管理","platformCode":"0002","parentId":180,"level":2,"url":"checkin","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":194,"cnName":"外教沟通管理","platformCode":"0002","parentId":180,"level":2,"url":"communication","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":193,"cnName":"监课记录","platformCode":"0002","parentId":180,"level":2,"url":"monitor","icon":"","sort":3,"childMenus":"","menuActions":""}],"menuActions":""},{"id":301,"cnName":"app管理","platformCode":"0002","parentId":0,"level":1,"url":"app-manage","icon":"","sort":18,"childMenus":[{"id":302,"cnName":"通讯列表","platformCode":"0002","parentId":301,"level":2,"url":"communication","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":304,"cnName":"升级管理","platformCode":"0002","parentId":301,"level":2,"url":"upgrade","icon":"","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":178,"cnName":"教学质量管理","platformCode":"0002","parentId":0,"level":1,"url":"quality","icon":"","sort":19,"childMenus":[{"id":187,"cnName":"外教评语","platformCode":"0002","parentId":178,"level":2,"url":"comment","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":188,"cnName":"Assessment","platformCode":"0002","parentId":178,"level":2,"url":"assessment","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":186,"cnName":"家长评价","platformCode":"0002","parentId":178,"level":2,"url":"assess","icon":"234","sort":3,"childMenus":"","menuActions":""}],"menuActions":""},{"id":154,"cnName":"外教TICO基础规则","platformCode":"0002","parentId":0,"level":1,"url":"foreign-tico","icon":"","sort":21,"childMenus":[{"id":155,"cnName":"分值与外教等级设置","platformCode":"0002","parentId":154,"level":2,"url":"level","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":157,"cnName":"指标与权重","platformCode":"0002","parentId":154,"level":2,"url":"weight-manager","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":244,"cnName":"函数配置","platformCode":"0002","parentId":154,"level":2,"url":"function-config","icon":"function-config","sort":3,"childMenus":"","menuActions":""}],"menuActions":""},{"id":153,"cnName":"外教TICO分数查询","platformCode":"0002","parentId":0,"level":1,"url":"tico-query","icon":"","sort":23,"childMenus":[{"id":156,"cnName":"TICO分数查看","platformCode":"0002","parentId":153,"level":2,"url":"view","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":166,"cnName":"TICO数据概览","platformCode":"0002","parentId":153,"level":2,"url":"overview","icon":"","sort":2,"childMenus":"","menuActions":""}],"menuActions":""},{"id":158,"cnName":"TICO指标数据维护","platformCode":"0002","parentId":0,"level":1,"url":"tico","icon":"","sort":25,"childMenus":[{"id":159,"cnName":"2.1外教行为规范评价","platformCode":"0002","parentId":158,"level":2,"url":"behaviour","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":160,"cnName":"2.2外教沟通评价","platformCode":"0002","parentId":158,"level":2,"url":"communication","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":161,"cnName":"3.1外教课堂教学评价","platformCode":"0002","parentId":158,"level":2,"url":"classroomteaching","icon":"","sort":3,"childMenus":"","menuActions":""},{"id":162,"cnName":"3.2外教培训评价","platformCode":"0002","parentId":158,"level":2,"url":"training","icon":"","sort":4,"childMenus":"","menuActions":""},{"id":163,"cnName":"3.5外教投诉","platformCode":"0002","parentId":158,"level":2,"url":"complaint","icon":"","sort":5,"childMenus":"","menuActions":""},{"id":240,"cnName":"试听分值","platformCode":"0002","parentId":158,"level":2,"url":"audition","icon":"audition","sort":5,"childMenus":"","menuActions":""},{"id":164,"cnName":"5.3外教录音数据统计","platformCode":"0002","parentId":158,"level":2,"url":"ticotape","icon":"","sort":6,"childMenus":"","menuActions":""},{"id":165,"cnName":"5.4外教培训数据统计","platformCode":"0002","parentId":158,"level":2,"url":"training-tape","icon":"","sort":7,"childMenus":"","menuActions":""}],"menuActions":""},{"id":177,"cnName":"工资管理","platformCode":"0002","parentId":0,"level":1,"url":"finance","icon":"","sort":27,"childMenus":[{"id":183,"cnName":"课时统计","platformCode":"0002","parentId":177,"level":2,"url":"class","icon":"","sort":1,"childMenus":"","menuActions":""},{"id":184,"cnName":"薪资管理","platformCode":"0002","parentId":177,"level":2,"url":"salary","icon":"","sort":2,"childMenus":"","menuActions":""},{"id":220,"cnName":"银行信息管理","platformCode":"0002","parentId":177,"level":2,"url":"bank-info","icon":"","sort":3,"childMenus":"","menuActions":""},{"id":185,"cnName":"个税表管理","platformCode":"0002","parentId":177,"level":2,"url":"tax","icon":"","sort":4,"childMenus":"","menuActions":""}],"menuActions":""},{"id":175,"cnName":"权限管理","platformCode":"0002","parentId":0,"level":1,"url":"authority","icon":"","sort":29,"childMenus":[{"id":176,"cnName":"分组管理","platformCode":"0002","parentId":175,"level":2,"url":"group","icon":"","sort":1,"childMenus":"","menuActions":""}],"menuActions":""},{"id":245,"cnName":"协同办公","platformCode":"0002","parentId":0,"level":1,"url":"wf-task","icon":"wf-task","sort":30,"childMenus":[{"id":246,"cnName":"我的协同","platformCode":"0002","parentId":245,"level":2,"url":"list","icon":"list","sort":1,"childMenus":"","menuActions":""}],"menuActions":""}],"dingTalkBindStatus":"","salerInfo":""}}
print(type(a))
b =jsonpath.jsonpath(a,'$.data.userInfoVO.token')
print(b[0])
