import unittest
import requests
from config.config import host,header1,logger





class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('-----登陆测试开始----------')
    def setUp(self):
        # print('登陆测试开始')
        self.url = host + '/sys/user/login'
        self.header = header1


    def test_login_ture(self):
        expect = 'success'
        res = requests.post(url=self.url,headers=self.header,json={"username":"xuxu002","password":"1234567"})
        # print(res)
        # print(res.text)
        logger.info(res.text)
        r = res.json()['msg']
        # print(r)
        self.assertEqual(r,expect)

    def test_login_username_error(self):
        expect = '用户名或密码错误'
        res = requests.post(url=self.url,headers=self.header,json={"username":"xuxu0021","password":"1234567"})
        logger.info(res.text)
        # print(res.text)
        r = res.json()['msg']
        # print (r)
        self.assertEqual(r,expect)

    def test_login_username_null(self):
        expect = '用户名或密码错误'
        r = requests.post(url=self.url,headers=self.header,json={"username":"","password":"1234567"}).json()['msg']

        # print(r)
        self.assertEqual(r,expect)

    def test_login_password_error(self):
        expect = '用户名或密码错误'
        r = requests.post(url=self.url, headers=self.header, json={"username": "xuxu002", "password": "123457"},timeout = 1).json()['msg']
        self.assertEqual(r,expect)

    def test_login_password_null(self):
        expect = '用户名或密码错误'
        r = requests.post(url=self.url, headers=self.header, json={"username": "xuxu002", "password": ""},timeout = 1).json()['msg']
        self.assertEqual(r,expect)

    def test_login_null(self):
        expect = '用户名或密码错误'
        r = requests.post(url=self.url, headers=self.header, json={"username": "", "password": ""}).json()['msg']
        self.assertEqual(r,expect)

    def tearDown(self):
        # print('登陆测试完毕')
        pass

    @classmethod
    def tearDownClass(cls):
        print('-----登陆测试结束----------')
# if __name__ == '__main__':
#     unittest.main()


