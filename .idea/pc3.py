#_*_coding:utf-8_*_
import urllib.request
import requests
from lxml import etree

html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents")
#print (html.text)
etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div/h4/a/text()')

for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)
