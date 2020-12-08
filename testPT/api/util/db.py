from api.view import serializer
import pymysql
import json
from api import models


class DB():

    def mysql(case,name,postpostposition): #定义一个函数，postpostposition是默认的参数

        result = 0
        print(f'{name}:接口开始数据库语句执行')
        postpostposition = json.loads(postpostposition)
        for i in postpostposition:

            dbname= i['key']

            key = models.Config.objects.filter(key=dbname)
            key = serializer.ConfigSerializer(key, many=True).data
            key = json.loads(json.dumps(key))

            dbparameter = key[0]['value']
            dbparameter = json.loads(dbparameter)
            dbparameter = dbparameter[0]
            host = dbparameter['host']
            user = dbparameter['user']
            password = dbparameter['password']
            db = dbparameter['db']
            port = int(dbparameter['port'])
            charset = dbparameter['charset']


            connection = pymysql.connect(host=host, user=user, password=password, db=db,port=port, charset=charset)
            cursor = connection.cursor()# 使用cursor()方法获取操作游标


            sql=i['value']
            try:
                print(1)
                a =cursor.execute(sql)#通过execute方法执行sql
                if a == 0:
                    result = +1
            except Exception as e:
                result = +1
                print(f'sql执行失败,具体错误如下：{e}')
            connection.commit()
            connection.close()  # 关闭数据库
            if result == 0:
                print('sql执行成功')
            else:
                print('sql执行失败')
        return result


# DB.mysql("update workflow_task_history set `status`='2' where id='1'")
