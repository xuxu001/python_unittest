# url = 'https://api.inewmaker.com/sys/user/login'
# header = {"Content-Type":"application/json"}
#             # "Authorization":"695927bb21f0019e910d254aa60a4b9b"}
# #
# # data ={
# #             "name": "5231",
# #             "password": "1234567",
# #             "roleIdList": [
# #                 1
# #             ],
# #
# #             "username": "xuxu008"
# #         }
# # import requests
# # res = requests.post(url = url,json=data,headers= header)
# # print(res.text)
# import requests
#
# res = requests.post(url=url,headers=header,json={"username":"xuxu002","password":"1234567"})
#
#
# print(res.text)
#
#coding:utf-8
from unittest import mock

url = 'https://www.baidu.com/'
import requests
r = requests.get(url)
a = r.text
print(r)
print(a.encode('utf-8'))

