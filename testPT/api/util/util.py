from api import models
from api.view import serializer
import jsonpath
import json
import pytest
import time
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import os
from api.test_case001 import TestOrder
from api.util.zipfile import zip_file
import  shutil
from pyDes import des, PAD_PKCS5, ECB
import base64

class Util():
    #获取用例执行的list
    def ApiSelect(data):
        TestOrder.error=[]
        TestOrder.rundata={}
        #根据入参查询用例list，然后循环调用执行用例
        model=jsonpath.jsonpath(data,'$..modular')[0]
        apiid = jsonpath.jsonpath(data, '$..api_id')[0]
        id = jsonpath.jsonpath(data, '$..id')[0]
        userid = jsonpath.jsonpath(data, '$..user')[0]
        TestOrder.rundata['runid']=id
        returndata ={}
        returndata['key']=userid
        #判断如果apiid不为null，则运行指定apiid的用例
        if apiid !='null':
            # runsave={}
            list = models.Api.objects.filter(id=apiid)
            list = serializer.ApiSerializer(list, many=True).data
            print('开始用例获取\n')
            lists = []
            for i in list:
                case = json.loads(json.dumps(i))
                lists.append(case)
            TestOrder.rundata['lists'] = lists
            TestOrder.rundata['runsave'] = apiid
            # runsave['lists']=lists
            # models.Run.objects.filter(id=id).update(runsave=runsave)
            print(f'本次测试用例集合为：{lists}\n')
            print(f'本次测试用例数量位：{len(lists)}\n')
        else:
            if model > 15:
                list = models.Api.objects.filter(modular=model)
                list = serializer.ApiSerializer(list, many=True).data
                print('开始用例获取\n')

                lists = []
                for i in list:
                    case = json.loads(json.dumps(i))
                    lists.append(case)
                TestOrder.rundata['lists'] = lists
                TestOrder.rundata['runsave'] = "null"
                print(f'本次测试用例集合为：{lists}\n')
                print(f'本次测试用例数量位：{len(lists)}\n')
            elif model < 15:
                #1.数据库查询获取模块列表，

                platformname = models.Modular.objects.filter(id=model)
                platformname = serializer.ModulerSerializer(platformname, many=True).data
                platformname = json.loads(json.dumps(platformname[0]))
                platformname = platformname['platform']
                #根据平台名称，查找模块列表
                modularlist = models.Modular.objects.filter(platform=platformname)
                modularname = serializer.ModulerSerializer(modularlist, many=True).data
                del modularname[0]
                modularlists = []
                for i in modularname:
                    modularname = json.loads(json.dumps(i))
                    modularid=modularname['id']
                    modularlists.append(modularid)
                #2.遍历模块列表获取每个模块的列表的数据，放在测试list里面，
                alllists=[]
                for i in modularlists:
                    list = models.Api.objects.filter(modular=i)
                    list = serializer.ApiSerializer(list, many=True).data
                    print('开始用例获取\n')


                    for i in list:
                        case = json.loads(json.dumps(i))
                        alllists.append(case)
                TestOrder.rundata['lists'] = alllists
                TestOrder.rundata['runsave'] = "null"
                print(f'本次测试用例集合为：{alllists}\n')
                print(f'本次测试用例数量位：{len(alllists)}\n')

            else:
                # 1.数据库查询获取模块列表，
                platforlist=[1,2,3,4,5,6,7,8,9]
                modularlists = []
                for i in platforlist:
                    platformname = models.Modular.objects.filter(id=i)
                    platformname = serializer.ModulerSerializer(platformname, many=True).data
                    platformname = json.loads(json.dumps(platformname[0]))
                    platformname = platformname['platform']
                    # 根据平台名称，查找模块列表
                    modularlist = models.Modular.objects.filter(platform=platformname)
                    modularname = serializer.ModulerSerializer(modularlist, many=True).data
                    del modularname[0]
                    for i in modularname:
                        modularname = json.loads(json.dumps(i))
                        modularid = modularname['id']
                        modularlists.append(modularid)
                # 2.遍历模块列表获取每个模块的列表的数据，放在测试list里面，
                alllists = []
                for i in modularlists:
                    list = models.Api.objects.filter(modular=i)
                    list = serializer.ApiSerializer(list, many=True).data
                    print('开始用例获取\n')

                    for i in list:
                        case = json.loads(json.dumps(i))
                        alllists.append(case)
                TestOrder.rundata['lists'] = alllists
                TestOrder.rundata['runsave'] = "null"
                print(f'本次测试用例集合为：{alllists}\n')
                print(f'本次测试用例数量位：{len(alllists)}\n')

        return returndata


        #开始执行测试，
    def nowrun(userid,runid):
        print(333)
        print(userid)
        repotrname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        address = os.getcwd()
        address = r"/".join(address.split("\\"))
        report_path_del = address+'/api/report'
        report_path = address+'/api/report.zip'
        file_names = report_path
        #防止上次执行错误，没有删除文件，所以删除测试报告
        try:
            os.remove(file_names)
            shutil.rmtree(report_path_del)
        except:
            pass



        pytest.main(['-k','test_001',f'--html=./api/report/{repotrname}.html'])
        # pytest.main([ f'--html=./api/report/{repotrname}.html'])

        # pytest.main(['-k', '-m','order','--arruredir=./api/report/allure'])

        #进行测试报告压缩
        report_path1 = address + '/api/report/'
        report_path2 = address + '/api'
        zip_file(report_path1, report_path2, 'report.zip', repotrname)

        #进行邮件发送通知
        key =models.User.objects.filter(id=userid)
        key = serializer.UserSerializer(key, many=True).data
        key = json.loads(json.dumps(key))
        receiver = key[0]['email']


        mail_body = len(Util.checkerrorlist(runid))
        Util.sendEmail(mail_body, receiver, file_names)

        #删除测试报告和文件
        os.remove(file_names)
        shutil.rmtree(report_path_del)


    def sendEmail( mail_body, receiver, file_names):
        """
        :param subject: 邮件标题
        :param mail_body: 邮件正文，可以是文字，也可以是html格式
        :param receiver: 邮件正文
        :param file_names: 邮件接收人
        :return:
        """
        if mail_body == 0:
            mail_body ='测试通过，仅供参考，详情见附件'
        else:
            mail_body='测试失败，具体看下面日志，可以搜索error字段'
        subject='自动化测试结果邮件'
        smtpserver = 'smtp.qq.com'  # smtp设置
        username = '2542726958@qq.com'  # 用户登陆账号
        password = 'kkcfmfihdzncecaj'  # 用户登陆密码

        msg = MIMEMultipart()
        # 邮件正文
        msg.attach(MIMEText(mail_body, 'plain', 'utf-8'))
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = username
        msg['To'] = receiver

        att = MIMEText(open(file_names, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="%s"' % (file_names)
        msg.attach(att)

            # 登录并发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(username, receiver.split(','), msg.as_string())
        except Exception as e:
            print(e)
            print("邮件发送失败！\n")
        else:
            print("邮件发送成功！\n")

        finally:
            smtp.quit()


    # 运行错误执行，进行结果添加
    # def dberror(testcase):
    #     TestOrder.error.append(testcase)

    def checkerrorlist(id):
        key = models.Cursor.objects.filter(run_id=id, usr_key='error')
        key = serializer.CursorSerializer(key, many=True).data
        if key == []:
            return []
        else:
            key = json.loads(json.dumps(key[0]))
            lists = json.loads(key['user_value'])
            return lists



    def errorlist(id,testcase):
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        key = models.Cursor.objects.filter(run_id=id, usr_key='error')
        key = serializer.CursorSerializer(key, many=True).data
        if key == []:
            lists = []
            lists.append(testcase)
            models.Cursor.objects.create(usr_key='error', user_value=lists, createtime=nowtime,
                                         api_id=testcase, run_id=id)
        else:
            key = json.loads(json.dumps(key[0]))
            lists =key['user_value']
            lists = json.loads(lists)
            lists.append(testcase)
            lists=str(lists)
            models.Cursor.objects.filter(run_id=id).update(user_value=lists, createtime=nowtime)

    def encryption(s):
        Des_Key = b"0d900510"
        k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
        encrystr = k.encrypt(s)
        return base64.b64encode(encrystr).decode('utf8')


    #获取单个用例结果
    def getrequest(data):
        id = jsonpath.jsonpath(data, '$..id')[0]
        data = models.Run.objects.filter(id=id)
        data = serializer.RunSerializer(data, many=True).data
        return data
    #进行相等校验
    def check_nodeText_equals(k,v,result,case,id):
        result = json.loads(result.text)
        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            Util.errorlist(id, case)
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
        if v.isdigit():
            route =int(v)
            print(f'开始判断{int(value)}是否等于{route}\n')
            try:
                assert int(value) == route, "对应的" +k+"值，不等于预期"+v
            except Exception as e:
                # TestOrder.error.append(case)
                Util.errorlist(id,case)
                print(f'error对应的{k}值不等于预期{value}：{e}\n')
        else:
            route = v
            print(f'开始判断{value}是否等于{route}\n')
            try:
                assert value == route, "对应的" + k + "值，不等于预期" + v
            except Exception as e:
                Util.errorlist(id, case)
                # TestOrder.error.append(case)
                print(f'error对应的{k}值不等于预期{route}值:{e}\n')


    #进行小于校验
    def check_nodeText_less(k,v,result,case,id):

        if k =='duration':
            value = round(result.elapsed.total_seconds()*1000)
            print(f'开始判断{value}是否小于{v}\n')
            try:
                assert int(value) < int(v), "对应的" + k + "值，大于预期" + v
            except Exception as e:
                # TestOrder.error.append(case)
                Util.errorlist(id, case)
                print(f'error对应的{k}值大于预期{v}值:{e}\n')
        else:
            result = json.loads(result.text)
            try:
                value = jsonpath.jsonpath(result, k)[0]
            except Exception as e:
                Util.errorlist(id, case)
                print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
            value = int(value)
            route = int(v)
            print(f'开始判断{value}是否小于{route}\n')
            try:
                assert value  <  route, "对应的" + k + "值，大于预期" + route
            except Exception as e:
                # TestOrder.error.append(case)
                Util.errorlist(id, case)
                print(f'error对应的{k}值不大于预期{route}值:{e}\n')
    #进行包含校验
    def check_nodeText_contains(k,v,result,case,id):
        result = json.loads(result.text)
        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            Util.errorlist(id, case)
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
        route = v
        print(f'开始判断{route}是否存在于{value}\n')
        try:
            assert route  in  value, "对应的" + k + "值，不包含预期" + route
        except Exception as e:
            # TestOrder.error.append(case)
            Util.errorlist(id, case)
            print(f'error对应的{value}值不包含预期{route}值:{e}\n')
    #进行参数长度校验
    def check_nodes_count(k,v,result,case,id):
        result = json.loads(result.text)
        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            Util.errorlist(id, case)
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
        route = v
        count=len(str(value))
        print(f'开始判断{value}的长度是否等于{int(route)}\n')
        try:
            assert count  ==  int(route), "对应的" + k + "值，长度不等于" + route
        except Exception as e:
            Util.errorlist(id, case)
            # TestOrder.error.append(case)
            print(f'error对应的{k}值长度不符合预期{route}值:{e}\n')












