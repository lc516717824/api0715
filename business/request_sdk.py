"""
自定义封装 request 请求
"""
import requests
from business.logger import loger
def do_request(url,http,params=None,data=None):
    if http == 'get':
        loger.debug(f"{http} {url} query params:{params}")
        res = requests.get(url,params)
        loger.debug(f'{res.json()} {res.status_code} {res.elapsed.total_seconds()}s')
        return res
    elif http == "post":
        loger.debug(f"{http} {url} data: {data}")
        res = requests.post(url=url, data=data)
        loger.debug(f'{res.json()} {res.status_code} {res.elapsed.total_seconds()}s')
        return res
    else:
        loger.error(f"{http}不是正确的http请求方法，请检查")