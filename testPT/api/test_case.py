from api.util import util
from api.util.testcase import Tesstcase
import pytest
import unittest
from api.util.mytest import Myunittest


class TestOrder(Myunittest):

    error =[]
    rundata = {}

    # @pytest.mark.order
    def test_001(self):
        runid = TestOrder.rundata['runid']
        rundata = TestOrder.rundata['lists']

        for i in rundata:
            print('------------------------------------------------------------------------------------------------------我是华丽的分界线-----'
                  '----------------------------------------------------------------------------------------')
            Tesstcase(i, runid).front()

        count = TestOrder.error
        print(f'本次用例执行完成，校验点失败数量：{len(count)}')
        print(count)
        assert 0==len(count)

if __name__ == '__main__':
    TestOrder.test_order_success_001()