from api import models
from api import serializer
import jsonpath
import json
import time
from api.data import HTMLTestRunner_cn
import pytest



from api.test_case import TestOrder
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import os

class Util():
    def ApiSelect(data):

        TestOrder.error=[]
        TestOrder.rundata={}
        #根据入参查询用例list，然后循环调用执行用例
        model=jsonpath.jsonpath(data,'$..modular')
        id = jsonpath.jsonpath(data, '$..id')[0]
        userid = jsonpath.jsonpath(data, '$..user')[0]
        TestOrder.rundata['runid']=id
        list = models.Api.objects.filter(modular=model[0])
        list =serializer.ApiSerializer(list,many=True).data
        print('开始用例获取\n')

        # for i in list:
        #     print('开始执行用例')
        #     case = json.loads(json.dumps(i))
        #     Tesstcase(case,id).front()
        lists =[]
        for i in list:
            case = json.loads(json.dumps(i))
            lists.append(case)
        TestOrder.rundata['lists']=lists
        print(f'本次测试用例集合为：{lists}\n')

        #开始进行测试

        repotrname = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        address = os.getcwd()
        address = r"/".join(address.split("\\"))
        report_path = address+'/api/report/' + repotrname + '.html'
        pytest.main(['-k','test_001',f'--html=./api/report/{repotrname}.html'])
        # pytest.main(['-k', '-m','order','--arruredir=./api/report/allure'])

        #进行邮件发送通知
        key =models.User.objects.filter(id=userid)
        key = serializer.UserSerializer(key, many=True).data
        key = json.loads(json.dumps(key))
        mail_body = len(TestOrder.error)
        receiver = key[0]['email']
        file_names = report_path
        Util.sendEmail(mail_body, receiver, file_names)

    def sendEmail( mail_body, receiver, file_names):
        """
        :param subject: 邮件标题
        :param mail_body: 邮件正文，可以是文字，也可以是html格式
        :param receiver: 邮件正文
        :param file_names: 邮件接收人
        :return:
        """
        if mail_body == 0:
            mail_body ='测试通过，详情见附件'
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

        # 附件:附件名称用英文
        # # for file_name in file_names:
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
            os.remove(file_names)
        finally:
            smtp.quit()

    # def check_reponse_total(vulue,result):
    #     assert result.status_code < vulue[3:] ,"接口相应时间超过"+k[3:]

    def check_nodeText_equals(k,v,result):
        route = v[6:]
        result = json.loads(result)
        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')

        if route.isdigit():
            route =int(v[6:])
            print(f'开始判断{int(value)}是否等于{route}\n')
            try:
                assert int(value) == route, "对应的" +k+"值，不等于预期"+route
            except Exception as e:
                TestOrder.error.append(k)
                print(f'error对应的{k}值不等于预期{value}：{e}\n')
        else:
            route = v[6:]
            print(f'开始判断{value}是否等于{route}\n')
            try:
                assert value == route, "对应的" + k + "值，不等于预期" + route
            except Exception as e:
                TestOrder.error.append(k)
                print(f'error对应的{k}值不等于预期{route}值:{e}\n')

    # def check_nodeText_notequals(k,v,result):
    #     route = v[3:]
    #     value = jsonpath.jsonpath(result, k)
    #     assert value != route, "对应的" + k + "值，不不等于预期" + value

    # def check_nodeText_greater(k,v,result):
    #     route = v[3:]
    #     value = int(jsonpath.jsonpath(result, k))
    #     assert value > route,  "对应的" + k + "值，不不等于预期" + value

    def check_nodeText_less(k,v,result):
        if k =='duration':
            route = int(v[6:])
            try:
                value = round(result.elapsed.total_seconds()*1000)
            except Exception as e:
                print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
            print(f'开始判断{value}是否小于{route}\n')
            try:
                assert int(value) < route, "对应的" + k + "值，大于预期" + route
            except Exception as e:
                TestOrder.error.append(k)
                print(f'error对应的{k}值不大于预期{route}值:{e}\n')
        else:
            route = int(v[6:])
            value = int(jsonpath.jsonpath(result, k))
            print(f'开始判断{value}是否小于{route}\n')
            try:
                assert value  <  route, "对应的" + k + "值，大于预期" + route
            except Exception as e:
                TestOrder.error.append(k)
                print(f'error对应的{k}值不大于预期{route}值:{e}\n')

    def check_nodeText_contains(k,v,result):
        route = v[6:]
        result = json.loads(result)

        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
        print(f'开始判断{route}是否存在于{value}\n')
        try:
            assert route  in  value, "对应的" + k + "值，不包含预期" + route
        except Exception as e:
            TestOrder.error.append(k)
            print(f'error对应的{k}值不包含预期{route}值:{e}\n')

    def check_nodes_count(k,v,result):
        route = v[6:]
        result = json.loads(result)
        try:
            value = jsonpath.jsonpath(result, k)[0]
        except Exception as e:
            print(f'error用例验证点路径找不到,具体错误如下：{e}\n')
        count=len(str(value))
        print(f'开始判断{count}的长度是否等于{int(route)}\n')
        try:
            assert count  ==  int(route), "对应的" + k + "值，长度不等于" + route
        except Exception as e:
            TestOrder.error.append(k)
            print(f'error对应的{k}值长度不符合预期{route}值:{e}\n')












