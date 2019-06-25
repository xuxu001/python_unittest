#coding:utf-8
#__author__ =='xuxu'
import unittest
import requests
from config.config import header, host, logger
from unittest import mock

class Test_package_add(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('--开始111--')
    def setUp(self):
        self.url = host + '/package/add'
        self.header = header

    #创建套餐，权益为已有的权益
    def test_package_add_001(self):
        url = self.url
        header = self.header
        data = {"name": "套餐名称", "price": "1000", "type": "1", "rightsList": [30005]}
        expect = {'msg': 'success'}
        database = {'msg': 'success'}
        res = requests.post(url=url, headers=header, json=data)
        data_mock = mock.return_value = database
        logger.info(res.text)
        res = data_mock
        r = res
        self.assertEqual(r, expect)

    #套餐名称大于12个字
    def test_package_add(self):
        url = self.url
        header = self.header
        data = {"name":"测试套餐名称大于十二个字了吗","price":"1000","type":"1","rightsList":[30005]}
        expect = '套餐名称大于12'
        res = requests.post(url=url,headers=header,json=data)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    #套餐价格非数字
    def test_package_add_price(self):
        url = self.url
        header = self.header
        data = {"name":"套餐名称","price":"好多","type":"1","rightsList":[30005]}
        expect = '价格不能非数字'
        res = requests.post(url,headers=header,json=data)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)
    #套餐名称重复
    def test_package_add_repeat(self):
        url = self.url
        header = self.header
        data = {"name":"套餐名称","price":"1000","type":"1","rightsList":[30005]}
        expect = '套餐名称重复'
        res = requests.post(url=url,headers=header,json=data)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    #按权益交付
    @unittest.skip
    def test_package_add_type_2(self):
        url = self.url
        header = self.header
        data = {"name":"测试套餐名称","price":"1000","type":"2","rightsList":[30005]}
        expect = 'success'
        res = requests.post(url=url,headers=header,json=data)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('--结束--')
