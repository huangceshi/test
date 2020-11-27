
from api.util.http import Http
import json
from api import models
from api.view import serializer
import jsonpath



class Tesstcase():

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
        self.postpostposition = case['case_postpostposition']
        self.runid=id
        self.apiid = apiid
        print(f'初始化测试用例id：{self.testcase}，测试昵称{self.testcase},请求方式：{self.type},请求地址：{self.url},请求值{self.data},上传文件名称{self.file_name},文件上传参数：{self.file_data}')

    def front(self):
        #之前之前，前置处理
        print(f'{self.testcase}开始请求前参数转化')
        #data 参数json化,如果是文件上传则不进行这个替换
        if self.data =='null':
            pass
        else:
            self.data = self.data.replace("'", "\"")
            self.data = json.loads(self.data)


        # replace 参数json化，替换参数进行json化
        if self.replace =='null':
            pass
        else:
            self.replace = self.replace.replace("'", "\"")
            self.replace = json.loads(self.replace)

        # save 参数json化  保存字段数据，进行json化
        if self.save == 'null':
            pass
        else:
            self.save = self.save.replace("'", "\"")
            self.save = json.loads(self.save)

        # check 参数json化 检查字段进行json参数化
        if self.check == 'null':
            pass
        else:
            self.check = self.check.replace("'", "\"")
            self.check = json.loads(self.check)

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



        if self.replace =='null':
            pass
        else:
            for k in self.replace.keys():
                #替换token，需要存在token
                if k == 'token':
                    key = models.Cursor.objects.filter(run_id=self.runid, usr_key=k)
                    value = serializer.CursorSerializer(key, many=True).data
                    value = jsonpath.jsonpath(value, '$..user_value')[0]
                    self.header['token']=value
                else:
                    key = models.Cursor.objects.filter(run_id=self.runid, usr_key=k)
                    value = serializer.CursorSerializer(key, many=True).data
                    value = jsonpath.jsonpath(value, '$..user_value')[0]
                    self.data[k]=value
        print('请求前参数替换完成')
        Tesstcase.execute_case(self)


        #执行用例
    def execute_case(self):
        """执行测试用例"""
        # -------------------------------------执行测试用例---------------------------------------
        print("============开始执行用例："+str(self.testname)+"=============")
        # #
        client = Http(method=self.type, url=self.url, data=self.data,file_name=self.file_name,file_data=self.file_data,header=self.header,name=self.testname,save=self.save,testcase=self.testcase,runid=self.runid )
        result =client.send()
        client.issave(self.save,result.text)
        client.checklist(self.check,result,self.testcase)
        client.processing(self.postpostposition)

        #判断如果是单接口运行，则存储测试结果，方便返回调用显示
        if self.apiid != 'null':
            resultlist=[]
            text=result.text.replace("\"", "'")
            resultlist.append(text)
            models.Run.objects.filter(id=self.runid).update(runsave=resultlist)






