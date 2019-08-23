#coding:utf-8
from urllib import request
import random
import time

url = 'http://people.rednet.cn/PeopleShow.asp?ID=3578557'

from src.user_agent_util import getheaders


def get_content(url):
    headers = getheaders()
    #Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = request.Request(url=url, headers=headers)
    content = request.urlopen(req).read().decode('utf-8')
    return content



pageviews = 10
for view in range(pageviews):
    print("第"+str(view)+"次模拟浏览记录!")
    page = get_content(url)
    sec = random.randint(0,10)
    time.sleep(5+sec)