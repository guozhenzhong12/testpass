import urllib.request
import urllib
import re
import os
import time


#图片url，我们百度首页logo下载下来
html = "https://www.buxiuse.com/"
result = urllib.request.urlopen(html)
picture = result.read()
content= result.read()
mystr = content.decode("utf8")
p=r"(http:\S{1,}.jpg)"
pattern = re.compile(p)
li = re.findall(pattern,mystr)
os.makedirs("D://image/",exist_ok=True)
for a in li:
    print("图片下载： "+a)
    b= a.split("/")[-1]
    urllib.request.urlretrieve(a, "D://image/"+b+".jpg")
    time.sleep(3)



