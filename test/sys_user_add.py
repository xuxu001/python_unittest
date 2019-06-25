import unittest
import requests
from config.config import header,host,logger
class Test_add_sys_user(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('--------------------------')
        print('-------开始添加用户接口------')
    def setUp(self):
        self.url = host + '/sys/user/add'
        self.header = header

    def test_add_sys_user_ture(self):
        data = {"password":"123456",
                "name":"123888",
                "roleIdList":[1],
                "username": "xuxu009",
                }
        expect = 'success'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data,headers = self.header)

        r = res.json()['msg']
        self.assertEqual(r,expect)

    def test_add_sys_user_username_repeat(self):
        data = {
            "name": "5231",
            "password": "1234567",
            "roleIdList": [
                1
            ],
            "userId": 0,
            "username": "xuxu008"
        }
        expect = '用户名已存在'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_long_username(self):
        data = {
            "name": "5231",
            "password": "1234567",
            "roleIdList": [
                1
            ],
            "userId": 0,
            "username": "xuxu008xuxu008xuxu008xuxu008"
        }
        expect = '用户名过长'

        res = requests.post(url=self.url, json=data,headers=self.header)
        print(res.text)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_shot_username(self):
        data = {
            "name": "5231",
            "password": "1234567",
            "roleIdList": [
                1
            ],
            "userId": 0,
            "username": "xu"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_Operation(self):
        data = {
            "name": "运营001",
            "password": "1234567",
            "roleIdList": [
                2
            ],
            "userId": 0,
            "username": "ceshi111"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url, json=data,headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_xs(self):
        data = {
            "name": "销售001",
            "password": "1234567",
            "roleIdList": [
                3
            ],
            "userId": 0,
            "username": "ceshi112"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)
    def test_add_sys_user_admin_operation(self):
        data = {
            "name": "admin+运营",
            "password": "1234567",
            "roleIdList": [
                1,2
            ],
            "userId": 0,
            "username": "ceshi113"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_admin_xs(self):
        data = {
            "name": "admin+销售",
            "password": "1234567",
            "roleIdList": [
                1,3
            ],
            "userId": 0,
            "username": "ceshi114"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_operation_xs(self):
        data = {
            "name": "运营+销售",
            "password": "1234567",
            "roleIdList": [
                2,3
            ],
            "userId":0,
            "username": "ceshi115"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    def test_add_sys_user_all(self):
        data = {
            "name": "admin+销售+运营",
            "password": "1234567",
            "roleIdList": [
                1,2,3
            ],
            "userId": 0,
            "username": "ceshi114"
        }
        expect = '用户名太短'
        logger.info(self.url, self.header, data, expect)
        res = requests.post(url=self.url,json=data, headers=self.header)
        logger.info(res.text)
        r = res.json()['msg']
        self.assertEqual(r, expect)

    @classmethod
    def tearDownClass(cls):
        print('添加用户接口结束')









