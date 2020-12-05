from api.util.http import Http
import json
from api import models
from api.view import serializer
import jsonpath
from  api.util import util


class Tesstcase():

    #初始化数据
    def __init__(self,case,id,apiid):

        self.testcase = case['id']
        self.testname = case['casename']
        self.type = case['case_type']
        self.url = case['case_url']
        self.data = case['case_data']
        self.replace = case['case_replace']
        self.file_name = case['case_file_name']
        self.file_data = case['case_file_data']
        self.check = case['case_check']
        self.save = case['case_save']
        self.status = case['case_status']
        self.postpostposition = case['case_postpostposition']
        self.runid=id
        self.apiid = apiid
        print(f'初始化测试用例id：{self.testcase}，测试昵称{self.testname},请求方式：{self.type},请求地址：{self.url},请求值{self.data},上传文件名称{self.file_name},文件上传参数：{self.file_data}'
              f',请求之前替换参数：{self.replace}，校验内容：{self.check}，保存参数：{self.save}，数据库操作参数：{self.postpostposition}')

    #参数替换
    def front(self):
        #之前之前，前置处理
        print(f'{self.testcase}开始请求前参数转化')

        #data
        self.data = json.loads(self.data)

        #替换header
        if self.type =='GET':
            self.header = {'Content-Type': 'application/json;charset=UTF-8'}
        else:
            if self.file_name =='null':
                self.header = {'Content-Type': 'application/json;charset=UTF-8'}
            else:
                #如果是文件上传，则替换文件上传请求的header
                self.header = {'Content-Disposition': 'form-data', 'Accept-Encoding': 'gzip',
                               'User-Agent': 'okhttp/3.11.0', 'Connection': 'keep-alive'}
                file_address = {'file': ('1', 'open(".api/data/upload/1", "rb")')}
                file_address = json.dumps(file_address)
                file_address =file_address.replace("1", self.file_name)
                file_address =json.loads(file_address)
                self.file_name =file_address

        if self.replace == '[]':
            pass
        else:
            try:
                self.replace = json.loads(self.replace)
                for i in self.replace:
                    key = i['key']
                    value = i['value']
                    if key == 'token':
                        value = models.Cursor.objects.filter(run_id=self.runid, usr_key=value)
                        value = serializer.CursorSerializer(value, many=True).data
                        value = jsonpath.jsonpath(value, '$..user_value')[0]
                        self.header['token']=value
                        pass
                    else:
                        value = models.Cursor.objects.filter(run_id=self.runid, usr_key=value)
                        value = serializer.CursorSerializer(value, many=True).data
                        value = jsonpath.jsonpath(value, '$..user_value')[0]
                        self.data[key]=value
            except:
                util.Util.dberror(self.testcase)

        #进行参数加密

        if self.status == '1':
            pass
        else:
            for i in self.data.keys():
                # 请求值加密
                value = util.Util.encryption(self.data[i])
                self.data[i] = value


        Tesstcase.completeurl(self)
    #补全ulr
    def completeurl(self):
        host = models.Config.objects.filter(key='测试环境')
        host = serializer.ConfigSerializer(host, many=True).data
        host = jsonpath.jsonpath(host, '$..value')[0]
        self.url = host + self.url
        print(self.url)
        Tesstcase.execute_case(self)
    #用例执行
    def execute_case(self):
        """执行测试用例"""
        # -------------------------------------执行测试用例---------------------------------------
        print("============开始执行用例："+str(self.testname)+"=============")
        # #
        client = Http(method=self.type, url=self.url, data=self.data,file_name=self.file_name,file_data=self.file_data,header=self.header,name=self.testname,save=self.save,testcase=self.testcase,runid=self.runid )
        result =client.send()
        #如果接口请求错误，则报错
        try:
            if json.loads(result.text)['code'] != 10000:
                util.Util.dberror(self.testcase)
                print(json.loads(result.text)['msg'])
                return result
            client.issave(self.save, result.text)
            client.checklist(self.check, result, self.testcase)
            client.processing(self.postpostposition)
        except:
            util.Util.dberror(self.testcase)


        #判断如果是单接口运行，则存储测试结果，方便返回调用显示
        if self.apiid != 'null':
            resultlist=[]
            text=result.text.replace("\"", "'")
            resultlist.append(text)
            models.Run.objects.filter(id=self.runid).update(runsave=resultlist)






