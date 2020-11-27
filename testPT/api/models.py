from django.db import models


# Create your models here.


class   User(models.Model):
    """用户表"""
    username = models.CharField(verbose_name='用户名',max_length=45,unique=True)
    password = models.CharField(verbose_name='密码',max_length=45)
    email = models.CharField(verbose_name='邮箱',max_length=45)


class Modular(models.Model):
    """模块表"""
    platform = models.CharField(verbose_name='平台',max_length=45,null=True)
    moduless =   models.CharField(verbose_name='模块名',max_length=45,null=True)
    status = models.CharField(verbose_name='模块状态', max_length=4, choices=(('1', '启用'),('2', '删除')), default='1')
    createtime =models.DateTimeField(verbose_name='创建时间')


class   Environmental(models.Model):
    """环境表"""
    es_name = models.CharField(verbose_name='环境名称',max_length=45,unique=True)
    es_ip = models.CharField(verbose_name='环境ip',max_length=45)
    es_port =models.CharField(verbose_name='环境端口号',max_length=45)
    es_user=models.CharField(verbose_name='环境用户名',max_length=45)
    es_password =models.CharField(verbose_name='环境密码',max_length=45)
    createtime = models.DateTimeField(verbose_name='创建时间')


class Api(models.Model):

    """用例表"""
    casename =models.CharField(verbose_name='用例名称',max_length=45,null=True)
    case_type =models.CharField(verbose_name='用例请求类型getpost等',max_length=45,null=True)
    case_url =models.CharField(verbose_name='用例请求地址',max_length=450,null=True,unique=False)
    case_data =models.CharField(verbose_name='用例请求参数',max_length=5000,null=True)
    case_replace=models.CharField(verbose_name='用例替换参数',max_length=4500,null=True)
    case_file_name=models.CharField(verbose_name='文件上传名称',max_length=500,null=True)
    case_file_data=models.CharField(verbose_name='上传文件接口请求参数',max_length=450,null=True)
    case_check=models.CharField(verbose_name='用例检查点',max_length=450,null=True)
    case_save =models.CharField(verbose_name='用例保存参数',max_length=1000,null=True)
    case_postpostposition = models.CharField(verbose_name='后置处理', max_length=4500,null=True)
    case_careatetime=models.DateTimeField(verbose_name='创建时间')
    case_status =models.CharField(verbose_name='用例状态', max_length=4, choices=(('1', '启用'),('2', '删除')), default='1')
    modular =models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=Modular)

class   Run(models.Model):
    """运行记录表"""
    run_url = models.CharField(verbose_name='运行结果链接',max_length=450,null=True)
    runsave = models.JSONField(verbose_name='运行结果链接', max_length=4500, null=True)
    createtime = models.DateTimeField(verbose_name='创建时间',null=True)
    modular = models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=Modular,null=True)
    user = models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=User ,null=True)
    api_id = models.CharField(verbose_name='执行id', max_length=45, null=True)

class Notice(models.Model):
    """消息通知表"""
    email_address=models.CharField(verbose_name='邮件地址',max_length=45)
    dingding=models.CharField(verbose_name='钉钉链接',max_length=200,null=True)
    notice_url=models.CharField(verbose_name='发送测试报告的地址',max_length=200)
    createtime=models.DateTimeField(verbose_name='创建时间')
    user = models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=User)

class   Cursor(models.Model):
    """临时表"""
    usr_key=models.CharField(verbose_name='保留字段名',max_length=4500)
    user_value=models.CharField(verbose_name='保留字段值',max_length=4500)
    createtime = models.DateTimeField(verbose_name='创建时间')
    run =models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=Run)
    api= models.ForeignKey(verbose_name='用户执行id', on_delete=models.CASCADE, to=Api)


class Config(models.Model):
    """配置表"""
    key =models.CharField(verbose_name='配置名称',max_length=45,unique=True)
    value = models.CharField(verbose_name='配置值', max_length=45,null=True)
    print()




