#!/usr/bin/python
# @Time ：2023.06.24
# @Author : Xie zy
# @File : weather_report.py
import json
import logging
import os
from datetime import datetime, timezone, timedelta
import requests

CALLBACK_URL = os.environ['CALLBACK_URL']
# specific
GAODE_API_KEY = os.environ['WEATHER_REPORT__GAODE_API_KEY']
WeChat_ID_LIST = os.environ['WEATHER_REPORT__WeChat_ID_LIST'].split(',', -1)


def send_to_wechat(msg):
    for wx_id in WeChat_ID_LIST:
        requests.post(url=CALLBACK_URL, json={
            "wxid": wx_id,
            "content": msg
        })


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

BJ_TIME_NOW = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
TODAY = BJ_TIME_NOW.strftime('%Y-%m-%d')

GAODE_URL = "https://restapi.amap.com/v3/weather/weatherInfo"

session = requests.Session()
params = {
    "key": GAODE_API_KEY,
    "city": "330782",
    "extensions": "all",
}
response = session.get(url=GAODE_URL, params=params)
res_dict = json.loads(response.text)
for cast in res_dict["forecasts"][0]["casts"]:
    if cast["date"] == TODAY and '雨' in cast['dayweather']:
        send_to_wechat("今天可能有雨哦，甜心记得带伞~")
