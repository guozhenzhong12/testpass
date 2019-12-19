import requests
import unittest


def test_example():
    url = "http://route.showapi.com/109-35", "my_appId", "my_appSecret"
    jaon_data = {
        "channelId": "",
        "channelName": "",
        "title": "足球",
        "page": "1",
        "needContent": "0",
        "needHtml": "0",
        "needAllList": "0",
        "maxResult": "20",
        "id": "",
    }
    response = requests.post(url, json=jaon_data)
    if requests.status_codes == 200:
        print(response.text)
        print("成功")
    else:
        print(response.text)
        print("失败")


class ShowapiRequest:
    pass


if __name__ == '__main__':
    unittest.main()
