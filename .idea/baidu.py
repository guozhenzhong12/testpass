import unittest
from selenium import webdriver
import unittest,time
import sys
import requests
help(requests)

class MyTestCase(unittest.TestCase):
    def test_cnblogs01(self):
        cnblogs_url = "http://www.cnblogs.com/yoyoketang/"
        response = requests.get(cnblogs_url)
        print (response.status_code)
        print (response.text)

    def test_cnblogs02(self):
        cnblogs_url = "http://zzk.cnblogs.com/s/blogpost?Keywords=yoyoketang"
        json_data = {
            "Keywords":"yoyoketang"
        }
        response = requests.get(cnblogs_url,json=json_data)
        print (response.status_code)
        print (response.text)

    def test_cnblogs04(self):
        cnblogs_url= ""



    def test_baidu03(self):
        baidu_url = "https://www.baidu.com/"
        response = requests.get(baidu_url)
        print (response.status_code)
        print (response.text)
        print (response.url)
        print (response.headers)
        print (response.cookies)


if __name__ == '__main__':
    unittest.main(test_baidu03)



#-- r.status_code     #响应状态码
#-- r.content           #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
#-- r.headers          #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#-- r.json()             #Requests中内置的JSON解码器
#-- r.url                  # 获取url
#-- r.encoding         # 编码格式
#-- r.cookies           # 获取cookie
#-- r.raw                #返回原始响应体
#-- r.text               #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
#-- r.raise_for_status() #失败请求(非200响应)抛出异常