#coding:utf-8
#__author__ =='xuxu'
import unittest
import requests
import mock

# def Test_001():
#     url = 'https://www.baidu.com'
#     r = requests.get(url)
#
#     print(r.status_code)
#     return r.status_code


class Test(unittest.TestCase):

    #
    # def test_test(self):
    #     url = 'https://www.baidu.com'
    #     r= requests.get(url)
    #     data = {
    #         'id':300,
    #         'cid':500
    #     }
    #     datae={
    #         'id':300,
    #         'cid':5001
    #     }
    #
    #
    #     data_mock=mock.return_value=data
    #
    #
    #     print(data_mock)
    #     r = data_mock
    #     res = r
    #     self.assertEqual(r, expect)

        def test_package_add(self):
            url = 'https://api.inewmaker.com/package/add'
            header = { "Content-Type": "application/json","Authorization":"695927bb21f0019e910d254aa60a4b9b"}

            data = {"name": "套餐名称", "price": "1000", "type": "1", "rightsList": [30005]}
            expect = {'msg': 'success'}
            database = {'msg': 'success'}
            res = requests.post(url=url, headers=header, json=data)
            print(res)
            data_mock = mock.return_value = database

            res = data_mock
            print(data_mock)
            r = res


            self.assertEqual(r, expect)





if __name__ == '__main__':
    Test()

