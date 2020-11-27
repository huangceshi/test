import requests
from requests.packages import urllib3
import jsonpath
from api import models
import time
import json
from api import serializer
from  api.util import util
from api.util.db import DB



class  Http():

    def __init__(self, method, url, data=None,file_name=None,file_data=None,header=None,name=None,save=None,testcase=None,runid=None):

        self.method = method
        self.url = url
        self.data = data
        self.file_name = file_name
        self.file_data = file_data
        self.header = header
        self.casename=name
        self.save =save
        self.testcase=testcase
        self.runid=runid

    def send(self):

        print(f'发送请求参数，请求用例：{self.casename},请求方式：{self.method},请求头：{self.header},请求链接：{self.url},请求体：{self.data},请求文件名称：{self.file_name},请求文件参数：{self.file_data}')
        # #忽略关闭ssl的安全警告
        urllib3.disable_warnings()

        try:
            if self.method == 'POST':

                if self.file_name == 'null':
                    self.response = requests.request(method=self.method, url=self.url, json=self.data,
                                                     headers=self.header, verify=False, timeout=5)
                    self.result = self.response
                else:
                    if self.file_data =='null':
                        self.response = requests.request(method=self.method, headers=self.header, url=self.url, files=self.file_name,
                                             verify=False, timeout=5)
                        self.result = self.response
                    else:
                        self.response = requests.request(method=self.method, headers=self.header, url=self.url,
                                                         files=self.file_name,data=self.file_data,
                                                         verify=False, timeout=5)
                        self.result = self.response


            elif self.method == 'GET':
                self.response = requests.request(method=self.method,url=self.url, json=self.data, headers=self.header, verify=False,timeout=5)
                self.result = self.response


            print(f'{self.casename}:请求反完成，返回结果：{self.result.text}')
            return self.result

        except Exception as e:
            print(f'{self.casename}:请求接口失败:{e}')




    def issave(self,data,result):
        #接口请求后，进行返回结果参数保存
        if data =='null':
            print(f'{self.casename}:接口不需要参数保存')
            pass
        else:
            print(f'{self.casename}:接口开始参数保存，保存参数为：{data}')
            result=json.loads(result)
            for k in data.keys():
                try:
                    value = jsonpath.jsonpath(result, '$..' + k)
                except Exception as e:
                    print(f'{self.casename}:接口参数保存格式写错：{e}')
                nowtime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                key =models.Cursor.objects.filter(run_id=self.runid,usr_key=k)
                key = serializer.CursorSerializer(key, many=True).data
                print(f'{self.casename}:接口开始参保存参数{k}的值{value[0]}')
                if key==[]:
                    models.Cursor.objects.create(usr_key=k, user_value=value[0], createtime=nowtime, api_id=self.testcase,run_id=self.runid)
                else:
                    models.Cursor.objects.update(usr_key=k, user_value=value[0], createtime=nowtime, api_id=self.testcase,run_id=self.runid)
            print(f'{self.casename}:接口参数保存成功完成')
    def checklist(self,checks,result,case):
        #接口请求后，对返回结果进行校验
        if checks == 'null':
            print(f'{self.casename}:接口没有校验点，不需要校验')
            pass
        else:
            print(f'{self.casename}:接口开始进行结果校验')
            for k in checks.keys():
                if checks[k][0:6]== 'check1':
                    util.Util.check_nodeText_equals(k,checks[k],result.text,case)
                elif checks[k][0:6]== 'check2':
                    util.Util.check_nodeText_less(k,checks[k],result,case)
                elif checks[k][0:6]== 'check3':
                    util.Util.check_nodeText_contains(k,checks[k],result.text,case)
                elif checks[k][0:6]== 'check4':
                    util.Util.check_nodes_count(k,checks[k],result.text,case)
                else:
                    print(self.testcase+"校验点不对，需要注意检查")
            print(f'{self.casename}:接口校验完成')

    def processing(self,postpostposition):
        if  postpostposition == 'null':
            print(f'{self.casename}:接口没有后置sql操作需要执行')
            pass
        else:
            DB.mysql(postpostposition)
            print(f'{self.casename}:接口开始进行后置sql执行:{postpostposition}')
        #
        #如果存储为list，则进行list循环操作
        # else:
        #     for i in postpostposition:
        #         DB.mysql(i)
        #         print(f'{self.casename}:接口开始进行后置sql执行:{postpostposition}')




    def Alert(msg):
        headers = {"Content-Type": "application/json"}
        data = {"msgtype": "text", "text": {"content": msg}}
        pass
        #待完善
        # r = requests.post(run.DATA['dingding'],data=json.dumps(data), headers=headers)
