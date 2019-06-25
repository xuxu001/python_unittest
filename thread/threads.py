# encoding=utf8
import threading
import requests
from datetime import  *
from config.config import host
#执行的线程数
Thread_num = 20
#循环的次数
one_worker_num = 10

def test():
    url = host + '/sys/user/login'
    data = {'username':'xuxu002','password':'1234567'}
    header = {'Content-Type':'application/json'}
    r = requests.post(url=url,json=data,headers=header)
    res = r.json()
    print(res)
    return res


def working():
    global one_worker_num
    for i in range(0,one_worker_num):
        test()

def t():
    global Thread_num
    Threads = []
    for i in range(Thread_num):
        t = threading.Thread(target=working())
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()

if __name__ == '__main__':
    t()