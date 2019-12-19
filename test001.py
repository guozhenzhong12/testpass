from selenium import webdriver
import unittest,time
import sys

class MyTestCase(unittest.TestCase):
    def test_login(self):
        print (sys.getdefaultencoding())
        self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        # 打开url
        self.driver.get("https://www.baidu.com/")
        time.sleep(3)
        # title = self.driver.title
        # print title
        # now_url = self.driver.current_url
        # print now_url
        # # 增加一个对url的校验
        # # assert
        username = "jcloud-b2c-03"
        # username = "业务研发Jdcloud_02"
        password = "Qa123456"
        # password = "Qa123456"
        # 用户名的定位
        self.driver.find_element_by_name('loginname').send_keys(username)
        # 密码的定位
        self.driver.find_element_by_id('nloginpwd').send_keys(password)
        # 点击登录
        self.driver.find_element_by_id("paipaiLoginSubmit").click()

        time.sleep(5)
        self.driver.get("http://cm-console.jcloud.com")
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
