#coding:utf-8

host = 'https://api.inewmaker.com'
header1 = {"Content-Type": "application/json"}
header =  { "Content-Type": "application/json","Authorization":"695927bb21f0019e910d254aa60a4b9b"}


import logging
import time
import sys
import os
now = time.strftime('%Y-%m-%d %H-%M')
#
report_path = os.path.join(os.getcwd(),'test_report')
filename = os.path.join(report_path,'api_log'+now+'.text')
# ft =open(file,'wb+')
#
# logging.basicConfig(filename=ft)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=filename,
                    filemode='w')
logger = logging.getLogger()