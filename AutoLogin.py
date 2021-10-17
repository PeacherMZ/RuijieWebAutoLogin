import requests
import time
import random

header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '955',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#   'Cookie': '',  #一定不要带Cookie，不然短时间重复访问会导致需要验证码
    'Host': '10.8.2.2',
    'Origin': 'http://10.8.2.2',
    'Referer': '',  #从请求头中获取
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'  #一般无需修改
}

dataLogin = {
    'userId': '',     #填写post请求中的账号
    'password': '',   #填写post请求中加密过的密码
    'service': '',    #选择网络接入方式，在post请求中有
    'queryString': '',#从post请求中复制过来即可
    'operatorPwd': '',          #不用填
    'operatorUserId': '',       #不用填
    'validcode': '',            #不用填
    'passwordEncrypt': 'true',  #不用修改      
    'userIndex': ''   #填写post请求中的对应字段
}

dataCheck = {
    'userIndex': ''   #填写post请求中的对应字段，同上
}

login = 'http://10.8.2.2/eportal/InterFace.do?method=login'                   #登录地址
checkStatus = 'http://10.8.2.2/eportal/InterFace.do?method=getOnlineUserInfo' #验证地址


def work():
    res1 = requests.post(url=checkStatus, headers=header, data=dataCheck)
    res1.encoding = 'utf-8'
    content = str(res1.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode())
    i = content.find('"result":"')
    #    print(content)
    if content[i + 10:i + 14] == 'wait':
        print(time.asctime(time.localtime(time.time())), "当前处于在线状态。")
    else:
        print(time.asctime(time.localtime(time.time())), "当前已经下线，正在尝试登录！")
        res2 = requests.post(url=login, headers=header, data=dataLogin)
        res2.encoding = 'utf-8'
        content2 = str(res2.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode())
        j = content2.find('"result":"')
        #        print(content2)
        if content2[j + 10:j + 17] == 'success':
            print(time.asctime(time.localtime(time.time())), "登录成功！")

while(True):
    try:
        work()
    except:
        print(time.asctime(time.localtime(time.time())), "监测出错，请检查网络是否连通。")
        time.sleep(1)
        continue
    time.sleep(random.randint(20, 40))  #这里间隔20~40秒查询一次状态，切莫太频繁
