import unittest
import requests
from Study_unittest.calculator import Calculator

a = "http://127.0.0.1"
class TestCalculator(unittest.TestCase):
    def test_add(self):
        a = 1
        b = 2
        c = a+b
        print(c)
    def test_add1(self):
        a = ["test", "wuyu"]
        b = ["libai", "zhans"]
        c = a+b
        print(c)

    def test_add2(self):

        b = "/tenant/new"
        c = a+b
        print(c)
        json_data = {
            "id": "dd69eebb35d640a1990ce6bcbac080b4",
            "name": "租户A",
            "ownerId": "21",
            "ownerName": "",
            "organizationName": "",
            "description": "",
            "products": "",
        }

        response = requests.post(url=c, json=json_data)
        if response.status_code == 200:
            print(response.text)
            print("新增用户测试通过")
        else:
            print ("http error info:%s" % response.status_code)
            print(response.text)
