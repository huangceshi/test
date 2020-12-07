#用于测试的文件夹


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
# urllib3.disable_warnings()
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



# a ={'key1':'value1','key2':'value2','key3':'value3'}
# print(len(a))
# print(a.keys())
# # for i in a:
# #     print(a)
# for i in a.keys():
#     #请求值加密
#     value = encryption(a[i])
#     a[i]=value



# const keyHex = CryptoJS.enc.Utf8.parse(key);
#     // 加密账号
#     const emailDES = CryptoJS.DES.encrypt(this.email, keyHex, {
#       mode: CryptoJS.mode.ECB,
#       padding: CryptoJS.pad.Pkcs7
#     }).toString();


# 秘钥
# 0d9005104cac49f693da6e6d46914f94


# {"userName":"WJ2tod/VMtdwffjX+ykjPA==","password":"GXuFOM+isDtwffjX+ykjPA=="}
#加密解密
# a = 'crmadmin'
# b =

from pyDes import des, CBC, PAD_PKCS5
import binascii

# 秘钥



# def des_encrypt(s):
#     KEY = '0d9005104cac49f693da6e6d46914f94'
#     """
#     DES 加密
#     :param s: 原始字符串
#     :return: 加密后字符串，16进制
#     """
#     KEY = bytes(KEY, encoding='utf-8')
#
#     secret_key = KEY
#     iv = secret_key
#     print(secret_key)
#     print(iv)
#     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
#     print(k)
#     en = k.encrypt(s, padmode=PAD_PKCS5)
#     print(en)
#     print(binascii.b2a_hex(en))
#     return binascii.b2a_hex(en)
#
# if __name__ == '__main__':
#     des_encrypt('Y3JtYWRtaW4=')


# public static void main(String[] args) {
#         String key = "0d9005104cac49f693da6e6d46914321";
#         String password = "password";
#         //加密
#         String encryptionPassword = SecureUtil.des(key.getBytes(StandardCharsets.UTF_8)).encryptBase64(password);
#         System.out.println(encryptionPassword);
#         //解密
#         String decryptPassword = SecureUtil.des(key.getBytes(StandardCharsets.UTF_8)).decryptStrFromBase64(encryptionPassword);
#         System.out.println(decryptPassword);
#     }
# java  ： Passwd.getBytes()
#
# python ： bytearray(passwd)
# import base64
from pyDes import des, PAD_PKCS5, ECB
# 想将字符串转编码成base64,要先将字符串转换成二进制数据
# url = "crmadmin"
# bytes_url = url.encode("utf-8")
# str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
# print(str_url)
#
# DES_SECRET_KEY ='0d9005104cac49f693da6e6d46914f94'
# des_obj = des(DES_SECRET_KEY, ECB, DES_SECRET_KEY, padmode=PAD_PKCS5)
# secret_bytes = des_obj.encrypt(str_url)
# print(secret_bytes)


# from Cryptodome.Cipher import DES
# import binascii
#
# def pad(text):
#     while len(text)%8 != 0: #不是8的倍数，用空格补全成8的倍数
#         text += ' '
#     return text

# key = b'abcdefgh' # 密钥,一般是8位或16位
# des = DES.new(key,DES.MODE_ECB) #参数 key:密钥 mode:模式一般是DES.MODE_ECB
# text = 'hello world' #要加密的文本
# encrypto_text = des.encrypt(pad(text).encode())# 加密
# print('密文',binascii.b2a_hex(encrypto_text)) #把bytes转成16进制
#
# # 如果不经过pad处理，会报错 ：加密的数据不对，必须是密钥的位数的整数倍（此处是8的整数倍）
# data = des.decrypt(encrypto_text).strip() # 会多出来一些字符串,所以要rstrip一下
# # data = des.decrypt(encrypto_text).decode('utf-8')
# print('明文',data)




# userName ='crmadmin'
# key = '0d9005104cac49f693da6e6d46914f94'
# iv ='0d9005104cac49f6'
# # 加密后

# key = bytes(key,encoding="utF-8")
# userName = bytes(userName,encoding="utF-8")
# iv = bytes(iv,encoding="utF-8")
# print(key)
# print(userName)
#
# k =des(key,CBC,iv,pad=None,padmode=PAD_PKCS5)
# en =K.encrypt(userName,padmode=PAD_PKCS5)
# print(en)


import base64
import pyDes

from pyDes import des, PAD_PKCS5, ECB

class PyDES3():
    def __init__(self, key):
        """
        三重DES加密、对称加密。py2下不可用
        :param key: 密钥
        """
        self.cryptor = pyDes.triple_des(key, padmode=pyDes.PAD_PKCS5)

    def encrypt(self, text):
        """
        加密
        :param text:
        :return:
        """
        x = self.cryptor.encrypt(text.encode())
        return base64.standard_b64encode(x).decode()

    def decrypt(self, text):
        """
        解密
        :param text:
        :return:
        """
        x = base64.standard_b64decode(text.encode())
        x = self.cryptor.decrypt(x)
        return x.decode()

if __name__ == '__main__':
    key = '0d9005104cac49f693da6e6d' # 此Key需与前端一致
    text = 'crmadmin'
    # key = key.encode()
    # text=text.encode()

    des = PyDES3(key)
    print(des.encrypt(text))
    print(des.decrypt('WJ2tod/VMtdwffjX+ykjPA=='))


# # userName= "WJ2tod/VMtdwffjX+ykjPA=="
