
import pymysql
class DB():
    def mysql(abc): #定义一个函数，abc是默认的参数
        connection = pymysql.connect(host='172.17.71.154', user='crm_test_user', password='EyH5O!8Wq!uJKAs3lP', db='crm_test_db',port=22809, charset='utf8')
        cursor = connection.cursor()# 使用cursor()方法获取操作游标
        sql=abc
        try:
            cursor.execute(sql)#通过execute方法执行sql
        except Exception as e:
            print(f'sql执行失败,具体错误如下：{e}')
        connection.commit()
        connection.close()  # 关闭数据库
        print(f'sql执行完成')


# DB.mysql("update workflow_task_history set `status`='2' where id='1'")