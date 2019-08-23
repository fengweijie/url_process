import pandas as pd
import pickle
import time
import requests
from src.user_agent_util import getheaders
filepath = "./all_proxy.csv"

def get_proxys(filepath):
    proxys = list()
    df_proxy = pd.read_csv(filepath,sep="\t")
    for protocol,ip in zip(df_proxy["代理协议"],df_proxy["代理IP"]):
        protocol = protocol.replace("代理","").split(",")[0].lower()
        if protocol == "http":
            proxy = 'http://' + ip
            proxies = {protocol:proxy}
        else :
            proxy = 'https://' + ip
            proxies = {protocol:proxy}
        proxys.append(proxies)
    return proxys


# with open("proxy.pkl","rb") as f:
#     lista = pickle.load(f)
#
# print(lista)
proxy_pool = []
proxys = get_proxys(filepath)
for req_proxy in proxys:
    header = getheaders()
    try:
        attempt = requests.get('http://www.baidu.com',headers= header,proxies = req_proxy,timeout=5)#注意这里使用IP的方式
        if attempt.status_code == 200:
            print('获得比较好的代理,地址:',req_proxy)
            proxy_pool.append(req_proxy)
    except Exception as e:
        print(e)

with open("proxy_0528.pkl","wb") as f:
    pickle.dump(proxy_pool,f)
