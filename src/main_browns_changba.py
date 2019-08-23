#coding:utf-8

import sys
sys.path.insert(0, '../src')

import pickle
import requests
from user_agent_util import get_mobi_headers
import random
import time


def get_proxy_list():
    with open("proxy_0528.pkl","rb") as f:
        proxys = pickle.load(f)
        print("合适的服务器数目：",len(proxys))
    return proxys


def get_req_proxy(proxys):
    req_proxy = random.choice(proxys)
    return req_proxy


#hpp_url = "http://people.rednet.cn/PeopleShow.asp?ID=3597465"
hpp_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx5948bce62ac34420&redirect_uri=https%3A%2F%2Fchangba.com%2Fs%2FVZxYs9LQdtwYKLFuL29j-w%3F%26cbcode%3DRkvQSz26klpktqOIHZgb_mW6qOn8LXpgAAG_ukrlk_fdHbkaIyTofgL-jDpq3_UeqJCOnTsftf8kdk1L4P2iC2P6rESiNsnI1jzaeDUCK8WXoWkL8jrEvf4-yv-OPqxs%26code%3DGt1bjDM0qnG_X60NZcKtO3UqvztDaccQvcLM425eHWtNvWKxI-6DfnvJ5vG4abzlPpkXyNQc665NLPp1mLgdJgmGAiMH3T6fh0dlpwrqlrQj64eti7jjmR-ONdIncsiK&response_type=code&scope=snsapi_base&state=STATE&connect_redirect=1#wechat_redirect"
#hpp_url = "http://people.rednet.cn/PeopleShow.asp?ID=3578557"
#hpp_url = "http://people.rednet.cn/PeopleShow.asp?ID=3597465"
#hpp_url = "https://www.toutiao.com/i6695378441664987651/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1559478447&app=news_article&utm_source=weixin&utm_medium=toutiao_android&req_id=201906022027260100250681998965C7D&group_id=6695378441664987651"

#hpp_url = "https://www.toutiao.com/i6595546041313919491/?tt_from=weixin&utm_campaign=client_share&wxshare_count=2&from=singlemessage&timestamp=1557119663&app=news_article&utm_source=weixin&utm_medium=toutiao_android&req_id=20190506131423010022056047081AB11&group_id=6595546041313919491&pbid=6687882509286852104"


def browns_url(number):
    sucess = 0
    proxys = get_proxy_list()
    for nu in range(number):
        header = getheaders()
        req_proxy = get_req_proxy(proxys)
        try:
            attempt = requests.get(hpp_url,headers= header,proxies = req_proxy,timeout=20)#注意这里使用IP的方式
            if attempt.status_code == 200:
                sucess = sucess +1
                print("第" + str(sucess)+'刷新成功',req_proxy,header)
                for i in range(10):
                    header = getheaders()
                    attempt = requests.get(hpp_url, headers=header, proxies=req_proxy, timeout=20)  # 注意这里使用IP的方式
                    if attempt.status_code == 200:
                        sucess = sucess + 1
                        print("第" + str(sucess) + '刷新成功', req_proxy,header)


        except Exception as e:
            print(e)

# browns_url(1000)

header = get_mobi_headers()
proxys = get_proxy_list()
req_proxy = get_req_proxy(proxys)
attempt = requests.get(hpp_url,headers= header,proxies = req_proxy,timeout=20)#注意这里使用IP的方式

print(attempt.text)
