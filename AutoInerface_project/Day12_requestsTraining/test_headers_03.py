#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_headers_03.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-09 11:02
# @Site    : 
# @version : V1.0

import requests
import json

# '''查询电话归属地'''
# data = {'mobileCode':'13018204373','userID':''}
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#
# r = requests.post(
#     url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
#     headers=headers,
#     data=data
# )
#
# print(r.text)

'''搜索拉勾网职位'''
data = {'first': False,'pn': 2,'kd': '测试架构师'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E6%9E%B6%E6%9E%84%E5%B8%88/p-city_252?&cl=false&fromSearch=true&labelWords=&suginput=',
    'Cookie': 'user_trace_token=20201220223538-cfbb423c-2c15-4152-bc47-43e10e2a8d89; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1608474939; _ga=GA1.2.2116100314.1608474939; LGUID=20201220223540-7b605482-842c-454e-b0f2-33e03c1ab556; JSESSIONID=ABAAABAABEIABCI8E5DC4C8E052BAB21E68852D58EB400E; WEBTJ-ID=20201220223856-1768096d33826-0a03ad737d8bee-59442e11-1098042-1768096d339117; _putrc=EE8ACE3018B6299B; login=true; unick=%E9%99%88%E5%AE%9D%E9%A1%BA; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; index_location_city=%E6%88%90%E9%83%BD; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20210109111219-4c2d12f8-826f-4f73-8573-4c61f91ad792; PRE_SITE=https%3A%2F%2Fwww.lagou.com; _gat=1; _gid=GA1.2.1541870551.1610161940; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=1c91b70a91642ad345916101616d5172ac606a5c62; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223180822%22%2C%22%24device_id%22%3A%221768094e62826-072eb916f62fca-59442e11-1098042-1768094e62a126%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2287.0.4280.88%22%7D%2C%22first_id%22%3A%221768094e62826-072eb916f62fca-59442e11-1098042-1768094e62a126%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1610161956; LGRID=20210109111235-e646d5b0-13af-4698-a60a-73861efd608e; SEARCH_ID=11b44edbbfae45f5b86c18274efd0bad'
}
params = {'needAddtionalResult': False}

r = requests.post(
    url='https://www.lagou.com/jobs/positionAjax.json',
    data=data,
    params=params,
    headers=headers
)

print(json.dumps(r.json(),indent=True,ensure_ascii=False))