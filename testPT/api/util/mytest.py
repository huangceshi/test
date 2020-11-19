
import unittest

class Myunittest(unittest.TestCase):
    pass
    #
    @classmethod
    def setUpClass(cls):
        pass
    #     udid=util.getXlsTesturl('url',0,1)
    #     run.DATA['udid'] = udid
    #     url =util.getXlsTesturl('url',1,1)
    #     run.DATA['url'] = url
    #     uploadurl = util.getXlsTesturl('url', 2, 1)
    #     run.DATA['uploadurl'] = uploadurl
    #     uid = util.getXlsTesturl('url', 3, 1)
    #     run.DATA['uid'] = uid
    #     dingding = util.getXlsTesturl('url', 4, 1)
    #     run.DATA['dingding'] = dingding
    #
    #     if 'qa' in url:
    #         test ='测试环境'
    #         run.DATA['test']=test
    #     else:
    #         test='线上环境'
    #         run.DATA['test'] = test
    #
    #     # #获取mysql1配置
    #     # mysqlname1 = util.getXlsTesturl('mysql', 1, 1)
    #     # run.DATAMYSQL['mysqlname1'] = mysqlname1
    #     # mysqlip1 = util.getXlsTesturl('mysql', 1, 2)
    #     # run.DATAMYSQL['mysqlip1'] = mysqlip1
    #     # mysqladmin1 = util.getXlsTesturl('mysql', 1, 3)
    #     # run.DATAMYSQL['mysqladmin1'] = mysqladmin1
    #     # mysqlpassworld1 = util.getXlsTesturl('mysql', 1, 4)
    #     # run.DATAMYSQL['mysqlpassworld1'] = mysqlpassworld1
    #     #
    #     # # 获取mysql2配置
    #     # mysqlname2 = util.getXlsTesturl('mysql', 1, 1)
    #     # run.DATAMYSQL['mysqlname2'] = mysqlname2
    #     # mysqlip2 = util.getXlsTesturl('mysql', 1, 2)
    #     # run.DATAMYSQL['mysqlip2'] = mysqlip2
    #     # mysqladmin2 = util.getXlsTesturl('mysql', 1, 3)
    #     # run.DATAMYSQL['mysqladmin2'] = mysqladmin2
    #     # mysqlpassworld2 = util.getXlsTesturl('mysql', 1, 4)
    #     # run.DATAMYSQL['mysqlpassworld2'] = mysqlpassworld2
    #     #
    #     # # 获取mysql3配置
    #     # mysqlname3 = util.getXlsTesturl('mysql', 1, 1)
    #     # run.DATAMYSQL['mysqlname3'] = mysqlname3
    #     # mysqlip3 = util.getXlsTesturl('mysql', 1, 2)
    #     # run.DATAMYSQL['mysqlip3'] = mysqlip3
    #     # mysqladmin3 = util.getXlsTesturl('mysql', 1, 3)
    #     # run.DATAMYSQL['mysqladmin3'] = mysqladmin3
    #     # mysqlpassworld3 = util.getXlsTesturl('mysql', 1, 4)
    #     # run.DATAMYSQL['mysqlpassworld3'] = mysqlpassworld3
    #     #
    #     # # 获取mysql4配置
    #     # mysqlname4 = util.getXlsTesturl('mysql', 1, 1)
    #     # run.DATAMYSQL['mysqlname4'] = mysqlname4
    #     # mysqlip4 = util.getXlsTesturl('mysql', 1, 2)
    #     # run.DATAMYSQL['mysqlip4'] = mysqlip4
    #     # mysqladmin4 = util.getXlsTesturl('mysql', 1, 3)
    #     # run.DATAMYSQL['mysqladmin4'] = mysqladmin4
    #     # mysqlpassworld5 = util.getXlsTesturl('mysql', 1, 4)
    #     # run.DATAMYSQL['mysqlpassworld5'] = mysqlpassworld5
    #     #
    #
    #
    #     host = url+'/token/request/'
    #     if uid ==str({}):
    #         data = {'plat': 1, 'udid': udid}
    #     else:
    #         data = {'plat': 1, 'udid': udid,'uid':uid}
    #     headers = {"Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded", "Accept": "*/*",
    #                "Accept-Encoding": "gzip, deflate", "User-Agent": "python-requests/2.22.0"}
    #     try:
    #         reponse = requests.request('POST', url=host, data=data, headers=headers,timeout=6)
    #         result = reponse.json()
    #         assert reponse.status_code == 200, http.http.Alert(test+'token请求返回状态码不是200')
    #         assert result.get('code') == 'A0000', http.http.Alert(test+'token请求失败，返回的不是A0000')
    #         token =result.get('data').get('token')
    #         print('token获取成功')
    #         run.DATA['token']=token
    #
    #
    #     except BaseException as  e:
    #         print('[token 获取失败]: 失败:', e.message)
    #         http.http.Alert(test+'token请求失败，超时')
    @classmethod
    def tearDownClass(cls):
        pass
        print('接口测试用例执行完毕')




if __name__ == '__main__':
    Myunittest()