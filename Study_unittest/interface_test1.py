# 2019-12-16
# Murray
import unittest
import requests
from Study_unittest.calculator import Calculator



class TestCalculator(unittest.TestCase):
    def test_add(self):
        url = "http://127.0.0.1"
        jehu = "/tenant/new"
        test1 = url + jehu
        print(test1)
        a = 1
        b = 2
        c = a + b
        print(c)
