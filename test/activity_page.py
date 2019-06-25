#coding:utf-8
import unittest
import requests
from config.config import header,host,logger

class Test_activity_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('---------------')
        print('---开始-----')

    def setUp(self):
        self.url =host +'/activity/page?title=&page=1&pageSize=10'
        self.header = header

    def test_1_10(self):
        url = self.url
        header = self.header
        expect = 'success'
        res = requests.get(url=url,headers= header)
        logger.info(res.text)

        r = res.json()['msg']
        self.assertEqual(r,expect)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('---结束---')

