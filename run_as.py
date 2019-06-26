import unittest
from HTMLTestRunner import HTMLTestRunner
from test.test_login import Test_login
from test.sys_user_add import Test_add_sys_user
from  test.student_page import Test_student_page
from test.activity_page import Test_activity_page
from test.sys_user_list import Test_sys_user_list
from test.package_add import Test_package_add
from test.package_list import Package_list
# from config.config import logger
from send_email.email import send_email
import os
import sys
report_path = os.path.join(os.getcwd(),'test_report')
print(report_path)
import time

def suite():



    test_login = unittest.makeSuite(Test_login,'test')

    test_add_sys_user = unittest.makeSuite(Test_add_sys_user,'test')
    test_student_page = unittest.makeSuite(Test_student_page,'test')
    test_activity_page = unittest.makeSuite(Test_activity_page,'test')
    test_sys_user_list = unittest.makeSuite(Test_sys_user_list,'test')
    test_package_add = unittest.makeSuite(Test_package_add,'test')
    test_package_list = unittest.makeSuite(Package_list,'test')
    Test = unittest.TestSuite([test_package_list,test_package_add,test_login,test_sys_user_list,test_student_page,test_activity_page,test_add_sys_user])

    return Test

# def report_address(reports_address):
#     test_reports_list = os.listdir(report_path)
#     new_test_reports_list = sorted(test_reports_list)
#     the_last_report = new_test_reports_list[-1]
#     the_last_report_address = os.path.join(reports_address,the_last_report)
#     return the_last_report_address

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M')



    filename = os.path.join(report_path,'api_test' + now + '.html')



    fp = open(filename, 'wb+')



    runner = HTMLTestRunner(stream=fp,title = '接口测试',description='描述',verbosity=1)
    runner.run(suite())


