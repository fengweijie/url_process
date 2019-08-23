import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
urls= 'https://www.xicidaili.com/nn/1'

def verification_url(url):
    s = requests.get(url,headers = headers)
    # print(s.text)
    return s, s.status_code

# get_xicidaili_proxys_tables(urls)

'''
<th>代理IP</th>
<th>代理协议</th>
<th>IP匿名度</th>
<th>代理位置</th>
<th>响应速度</th>
<th>存活时间</th>
<th>最后验证时间</th>
<th>打分</th>
'''
xiladaili = "http://www.xiladaili.com/gaoni/1/"
data_list = []
s, status_code = verification_url(xiladaili)
if status_code == 200:
    soup = BeautifulSoup(s.text,'lxml')
    tables = soup.find_all('table',class_='fl-table')[0]
    tags = soup.find_all('tr')
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
data_list.to_csv("../proxy/base_proxy.csv",sep="\t")



