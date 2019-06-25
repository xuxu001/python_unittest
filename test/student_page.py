#coding:utf-8
import unittest
import requests
from config.config import header,host,logger

class Test_student_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('--------------------------')
        print('-------开始查看学员列表接口------')

    def setUp(self):
        self.url = host + '/student/page'
        self.header = header
    #获取前10个
    def test_student_page(self):
        url = self.url
        header = self.header
        data = {"page":1,"pageSize":10,}
        expect = 'success'
        logger.info(url, header, data, expect)
        res = requests.post(url = url,json=data,headers = header,)
        logger.info(res.text)
        print(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)

    def test_student_page_add(self):
        expect = 'success'
        url = self.url
        header = self.header
        data = {"page":1,"pageSize":100,}
        logger.info(url,header,data,expect)
        res = requests.post(url=url,json=data,headers=header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r,expect)


    def tearDown(self):

        pass



    @classmethod
    def tearDownClass(cls):
        print('添加用户接口结束')