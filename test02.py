#coding=utf-8
import unittest
import requests

import json
class queryPermissionDetailV1(unittest.TestCase):
    def test01_authenticate(self):
        queryPermissionDetailV1_url = 'http://cm-biz-stag.jdcloud.com/user?action=queryPermission'
        #heders = {"Content-Type":"application/json"}
        json_data = {
            "permission":"485",
            "account":"guhao002",
            "user":"guhao002"
        }
        response = requests.post(url=queryPermissionDetailV1_url, json=json_data)
        if response.status_code == 200:

            #response.encoding = response.apparent_encoding
            #response = json.loads(response.text)
            print(response.text);
        else:
            #print response.json().get('message')
            print ("http error info:%s" % response.status_code)
            print(response.text)
    def test02_queryPermissionDetailV1(self):
        authenticate1_url = 'http://cm-biz-stag.jdcloud.com//user?action=authenticate'
        json_data = {
            "account":"guhao002",
            "user":"jcloud_zkwWpeu",
            "infos":[
                {
                    "action": "csa:queryStatisticsEventTrend",
                    "resource":"jrn:csa:cn-north-1::csa"
                }
            ]
        }
        response = requests.post(url=authenticate1_url, json=json_data)
        if response.status_code == 200:
            # response.encoding = response.apparent_encoding
            # response = json.loads(response.text)
            print(response.text)
        else:
            # print response.json().get('message')
            print ("http error info:%s" % response.status_code)
            print(response.text)
    def test03_authenticate(self):
        queryPermissionDetailV1_url = 'http://cm-biz-stag.jdcloud.com/user?action=queryPermissionDetailV1'
        json_data = {
            "permission": "485",
            "account": "guhao002",
            "user": "guhao002"
        }
        response = requests.post(url=queryPermissionDetailV1_url, json=json_data)
        if response.status_code == 200:
            print(response.text)
        else:
            print ("http error info:%s" % response.status_code)
            print(response.text)
            print("test fiad")


if __name__ == '__main__':
    unittest.main()
