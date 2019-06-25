#encoding=utf-8
import threading
import requests
import time


Thread_num = 100

one_worker_num = 50

def test():
    time.sleep(5)
    url = 'https://multi-chat.jihepai.com/api/web/group/message/create/crowd'
    header = {'Content-Type':'application/json','authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDAwNSIsInJvbGVzIjpbImFkbWluIl0sImV4cCI6MTU2MTE4NDU5NH0.xX331L7Ep4W9hR-S2K2lgfPW73BnWlGNxzFTbb_gdXc'}
    data = {"messageContents":[{"content":"111","createTime":1560927022000,"msgType":1,"orderId":1},{"content":"2","createTime":1560927022000,"msgType":1,"orderId":2},{"content":"333","createTime":1560927022000,"msgType":1,"orderId":3},{"content":"4","createTime":1560927022000,"msgType":1,"orderId":4},{"content":"555","createTime":1560927022000,"msgType":1,"orderId":5}],"sendTime":"2019-06-19 14:50:12","tagIds":"150041","teamId":30005}
    r = requests.post(url=url,json= data,headers=header)
    print(r.text)
    print(r.status_code)

    return r


def working():
    global one_worker_num
    for i in range (0,one_worker_num):
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
