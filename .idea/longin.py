# coding:utf-8
# coding:utf-8
import requests
# 禅道host地址
host = "http://127.0.0.1"

def login(s,username,psw):
    url = host+"/zentao/user-login.html"

    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": host+"/zentao/user-login.html",
        # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    body1 = {"account": username,
             "password": psw,
             "keepLogin[]": "on",
             "referer":  host+"/zentao/my/"
             }

    # s = requests.session()   不要写死session

    r1 = s.post(url, data=body1, headers=h)
    # return r1.content  # python2的return这个
    return r1.content.decode("utf-8")  # python3

def is_login_sucess(res):
    if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
        return False
    elif "parent.location=" in res:
        return True
    else:
        return False

if __name__ == "__main__":
    s = requests.session()
    a = login(s, "admin", "e10adc3949ba59abbe56e057f20f883e")
    result = is_login_sucess(a)
    print("测试结果：%s"%result)