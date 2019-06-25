#coding:utf-8
#__author__ =='xuxu'
#获取用户列表接口
import unittest
import requests
from config.config import header,host,logger

class Test_sys_user_list(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('---开始---')

    def setUp(self):
        self.url = host + '/sys/user/list'
        self.header = header

    #获取系统用户列表
    def test_sys_list(self):
        url = self.url + '?roleld=1'
        header = self.header
        expect = 'success'
        res = requests.get(url=url,headers=header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    #获取运营用户李彪
    def test_yun_list(self):
        url = self.url +'?roleld=2'
        header = self.header
        expect = 'success'
        res = requests.get(url=url,headers=header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    #获取销售用户列表
    def test_sales_list(self):
        url = self.url + '?roleld=3'
        header = self.header
        expect = 'success'
        res = requests.get(url=url,headers=header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('--结束--')
