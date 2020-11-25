# # -*- coding: utf-8 -*-
# # @Time    : 2019/9/19 13:46
# # @Author  : HuangWenjun
# # @Email   : 350920551@qq.com
# # @File    : send_mail.py
# # @Software: PyCharm
# # from email.mime.multipart import MIMEMultipart
# # from email.header import Header
# # from email.mime.text import MIMEText
# # import smtplib
#
#
# def sendEmail(subject, mail_body, receiver, file_names=list()):
#     """
#     :param subject: 邮件标题
#     :param mail_body: 邮件正文，可以是文字，也可以是html格式
#     :param receiver: 邮件正文
#     :param file_names: 邮件接收人
#     :return:
#     """
#     smtpserver = 'smtp.qq.com'  # smtp设置
#     username = '2542726958@qq.com'  # 用户登陆账号
#     password = 'kkcfmfihdzncecaj'  # 用户登陆密码
#
#     msg = MIMEMultipart()
#     # 邮件正文
#     msg.attach(MIMEText(mail_body, 'plain', 'utf-8'))
#     msg['Subject'] = Header(subject, 'utf-8')
#     msg['From'] = username
#     msg['To'] = receiver
#
#     # 附件:附件名称用英文
#     for file_name in file_names:
#         att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
#         att["Content-Type"] = 'application/octet-stream'
#         att['Content-Disposition'] = 'attachment;filename="%s"' % (file_name)
#         msg.attach(att)
#
#         # 登录并发送邮件
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)
#         smtp.login(username, password)
#         smtp.sendmail(username, receiver.split(','), msg.as_string())
#     except Exception as e:
#         print(e)
#         print("邮件发送失败！")
#     else:
#         print("邮件发送成功！")
#     finally:
#         smtp.quit()
#
#
# if __name__ == '__main__':
#     subject = "自动化测试结果邮件"
#     mail_body = "测试本文"
#     receiver = "huangxiaowei1@xdf.cn"  # 接收人邮件地址 用逗号分隔
#     file_names = ['C:\\Users\\bling\\PycharmProjects\\testPT\\api\\report\\2020-11-18-08-22-17.html']
#     sendEmail(subject, mail_body, receiver, file_names)
#     import os
#
#     print(os.getcwd())
# b ={}
# a =[{'id': 11, 'platform': '基础业务线', 'moduless': '模块1', 'status': '1', 'createtime': '2020-11-10T16:39:00'}, {'id': 12, 'platform': '基础业务线', 'moduless': '模块2', 'status': '1', 'createtime': '2020-11-10T16:39:00'}]
# print(type(a))
# b['key']=a
# print(b)

# list = [{'基础业务线': 1}, {'外教业务线': 2}, {'用户端业务线': 3}, {'教学业务线': 4}, {'增长业务线': 5}, {'活动课件': 6}, {'课程顾问': 7}, {'备用业务线1': 8},
#         {'备用业务线2': 9}]
#
# print(list[0])
# print(type(list[0]))


a =[1,2]
for i in a:
    print(i)






