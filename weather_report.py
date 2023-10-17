#!/usr/bin/python
# @Time ：2023.06.24
# @Author : Xie zy
# @File : weather_report.py
import json

from common import *

GAODE_API_KEY = os.environ['GAODE_API_KEY']
WeChat_ID_LIST = os.environ['WeChat_ID_LIST'].split(',', -1)
TODAY = getBJTodayDateStr()
GAODE_API_URL = "https://restapi.amap.com/v3/weather/weatherInfo"

# start...
startLogging()
session = requests.Session()
params = {
    "key": GAODE_API_KEY,
    "city": "330782",
    "extensions": "all",
}
response = session.get(url=GAODE_API_URL, params=params)
res_dict = json.loads(response.text)
for cast in res_dict["forecasts"][0]["casts"]:
    if cast["date"] == TODAY and '雨' in cast['dayweather']:
        batch_send_to_wechat(TODAY + "今天白天可能有" + cast['dayweather'] + "，甜心记得带伞哦，不要忘了呀~", WeChat_ID_LIST)
