#coding:utf-8
#__author__ =='xuxu'
import unittest
import requests
from config.config import header, host, logger


class Package_list(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('----start-------')
    def setUp(self):
        self.url=host+'/package/list'
        self.header = header

    def test_package_list(self):
        expect = 'success'
        res = requests.get(url=self.url,headers = self.header)
        r = res.json()['msg']
        # logger.info(res.text)
        self.assertEqual(r,expect)
        print(r)
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        print('----end---')
