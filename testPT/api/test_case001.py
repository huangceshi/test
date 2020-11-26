
from api.util.testcase import Tesstcase
from api.util.mytest import Myunittest
# from api.util.util import Util

class TestOrder(Myunittest):

    error =[]
    rundata = {}

    # @pytest.mark.order
    def test_001(self):
        runid = TestOrder.rundata['runid']
        rundata = TestOrder.rundata['lists']
        apiid = TestOrder.rundata['runsave']
        print(f'本次测试用例数量问：{len(rundata)}\n')
        print(f'本次测试用例集合为：{rundata}\n')


        for i in rundata:
            print('------------------------------------------------------------------------------------------------------我是华丽的分界线-----'
                  '----------------------------------------------------------------------------------------')

            Tesstcase(i, runid, apiid).front()

        count = TestOrder.error
        print(f'本次用例执行完成，校验点失败数量：{len(count)}')
        print(count)
        assert 0==len(count)

