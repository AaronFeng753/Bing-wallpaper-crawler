#coding=utf-8

import requests
import re
import os

print('获取图片中.....')

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
r1=requests.get('https://www.bing.com/',headers=headers)

p1 = re.compile(r'/th\Wid=OHR\S+jpg')
res1 = p1.findall(r1.text)

r2=requests.get('https://www.bing.com/'+res1[0],headers=headers)
with open('BingWallpaper.jpg','wb+') as f:
	f.write(r2.content)
	
print('\n图片已保存为 BingWallpaper.jpg')
input()
