import urllib.request
#图片url，我们百度首页logo下载下来
picture_url = "https://tva1.sinaimg.cn/bmiddle/0080xEK2gy1g8zv5albt4j30u00u040y.jpg"
result = urllib.request.urlopen(picture_url)
picture = result.read()
#创建图片文件
with open(r"D:\image\baidu_logo.png", "wb") as f:f.write(picture)

#写入二进制数据
