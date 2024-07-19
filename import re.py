from lxml import etree
import re
import requests

'''
url_music_yun='https://m801.music.126.net/20240606205628/1e929984d224c658a9f64509b598e23d/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/36375816708/02a5/ba52/0ba2/41e719e2b857264bff26dddfd65a4bd3.m4a'
video_0 = 'https://v26-web.douyinvod.com/fa4476132856a1d47b2e542692298c7e/6661ce04/video/tos/cn/tos-cn-ve-15c001-alinc2/oYPlCFDA9AAiMEZOSgEIjKBA8Q0gwoEFYmfe2Z/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=357&bt=357&cs=0&ds=4&ft=LjhJEL998xXdu4PP10P5fQhlpPiXEa3ExVJEAS93RbPD-Ipz&mime_type=video_mp4&qs=0&rc=OGc1ODQ0aDk8ZTtlOjc4aEBpM3VlZm45cjZpczMzNGkzM0AxLjMwLzYzNTQxYDYtXy9gYSNjaGA2MmRrMmRgLS1kLS9zcw%3D%3D&btag=80000e00028000&cquery=100z_100a_101s_100B_100x&dy_q=1717678464&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240606205423D71F85F933CC8E0A523C'
request_0 = requests.get(url_music_yun)
resou_0=request_0.content
with open ('music_0.mp3','wb') as f:
    f.write(resou_0)
request_1=requests.get(video_0)
resou_1=request_1.content
with open ('video_0.mp4','wb') as f:
    f.write(resou_1)
'''
'''
url_music_kugou='https://webfs.hw.kugou.com/202406062122/dc4faff5d39d8766dfe58100f664390e/KGTX/CLTX001/d06928b1252de5f736f96652d8e54657.mp3'
request_kugou=requests.get(url_music_kugou)
resou_kugou=request_kugou.content
with open ('music_kugou.mp3','wb') as f:
    f.write(resou_kugou)

a=['php','python',['苹果','梨子','桃子','西瓜'],'c','前端']
for i in a[2]:
    print(i)
'''


'''text = "https://www.runoob.com/python3/python3-examples.htmlhttps://www.runoob.com/python3/python3-examples.htmlhttps://www.runoob.com/python3/python3-examples.html"

pattern = r'https?://\S+?(?=(https?://|\s|\Z))'
urls = re.findall(pattern, text)
print(urls)
# 输出: ['https://www.runoob.com/python3/python3-examples.html', 'https://www.runoob.com/python3/python3-examples.html', 'https://www.runoob.com/python3/python3-examples.html']'''

'''str_url='https://www.runoob.com/python3/python3-examples.html,https://www.runoob.com/python3/python3-examples.html,https://www.runoob.com/python3/python3-examples.html'
aa = re.findall(, str_url)
print(aa)'''

path_nov = './test_file/nov_html.txt'
# print(1%3)
url_0 = 'https://www.hongxiu.com/chapter/27263292302202504/73745320881739928'
url_1 = 'https://www.hongxiu.com/book/27263292302202504#Catalog'
nov_request = requests.get(url_0)
nov_resou = nov_request.text
# s使用etree解析网页源码中的html
html_0 = etree.HTML(nov_resou)
with open(path_nov, 'w', encoding='utf-8') as f:
    f.write(nov_resou)
# 获取章节标题
a = '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/p/text()'
# title_0=html_0.xpath('//div[@class="book-title"]/h1/text()')[0]
# 获取章节内容
content_0 = html_0.xpath('a ')
print(content_0)
# 输出章节标题和内容


biaoqian_0 = '/html/body/div[1]/div[2]/div[4]/div[4]/div[2]/div[1]/ul[1]/li/a'
nov_request_1 = requests.get(url_1)
nov_resou_1 = nov_request.text
# s使用etree解析网页源码中的html
html_0 = etree.HTML(nov_resou_1)
for i in html_0.xpath(biaoqian_0):
