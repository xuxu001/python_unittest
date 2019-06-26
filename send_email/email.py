#coding:utf-8
#__author__ =='xuxu'
import unittest
import requests
from config.config import header, host, logger
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time


def send_email(file_name):
    smtpserver = 'smtp.163.com'
    send_user_name = 'j18682948872@163.com'
    send_user_password = 'jiaxu321'
    recode_user_name = '651379705@qq.com'
    send_name = 'assiass'
    subject = '接口测试报告'
    f = open(file_name,'rb+')
    mail_body = f.read()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(subject,charset='utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(send_user_name,send_user_password)
    smtp.sendmail(send_user_name,recode_user_name.split(','),msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_email()



