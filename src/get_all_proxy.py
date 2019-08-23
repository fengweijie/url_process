import requests
from bs4 import BeautifulSoup
import pandas as pd
from src.user_agent_util import getheaders

def verification_url(url):
    headers = getheaders()
    s = requests.get(url,headers = headers)
    return s, s.status_code


def get_xiladaili_page_info(index):
    xiladaili = "http://www.xiladaili.com/gaoni/"
    url = xiladaili + str(index)+"/"
    data_list = []
    s, status_code = verification_url(url)
    if status_code == 200:
        soup = BeautifulSoup(s.text,'lxml')
        tables = soup.find_all('table',class_='fl-table')[0]
        tags = tables.find_all('tr')
        for idx, tag in enumerate(tags):
            if idx!=0:
                tds = tag.find_all('td')
                data_list.append({
                    "代理IP": tds[0].contents[0],
                    "代理协议": tds[1].contents[0],
                    "IP匿名度": tds[2].contents[0],
                    "代理位置": tds[3].contents[0],
                    "响应速度": tds[4].contents[0],
                    "存活时间": tds[5].contents[0],
                    "最后验证时间": tds[6].contents[0],
                    "打分": tds[7].contents[0],
                })

    data_list = pd.DataFrame(data_list)
    filepath = "../proxy/base_proxy_"+str(index)+"_.csv"
    data_list.to_csv(filepath,sep="\t")


all_proxy = pd.DataFrame()
for index in range(0,35):
    filepath = "../proxy/base_proxy_" + str(index) + "_.csv"
    df_data = pd.read_csv(filepath,sep="\t")
    all_proxy = all_proxy.append(df_data,ignore_index=True)
all_proxy.to_csv("./all_proxy.csv",sep="\t",index=False)

# 爬取代理服务器
# import time
# for index in range(1,50):
#     get_xiladaili_page_info(index)
#     print("第n次请求,n=",index)
#     time.sleep(10)



# def verification_url_using_proxy(url):
#
#     headers = getheaders()
#     s = requests.get(url,headers = headers)
#     return s, s.status_code




# index = 32
# filepath = "../proxy/base_proxy_"+str(index)+"_.csv"
# df_proxy = pd.read_csv(filepath,sep="\t")
# proxys = list()
# for protocol,ip in zip(df_proxy["代理协议"],df_proxy["代理IP"]):
#     protocol = protocol.replace("代理","").split(",")[0].lower()
#     if protocol == "http":
#         proxy = 'http://' + ip
#         proxies = {protocol:proxy}
#     else :
#         proxy = 'https://' + ip
#         proxies = {protocol:proxy}
#     proxys.append(proxies)



# http_url = 'http://people.rednet.cn/PeopleShow.asp?ID=3578557'
# for pro in proxys:
#     try:
#         headers = getheaders()
#         page_info = requests.get(http_url, headers=headers,proxies=pro,timeout=30)
#         print(page_info.status_code)
#     except Exception as e:
#         print(e)
