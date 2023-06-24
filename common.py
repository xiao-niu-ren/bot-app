#!/usr/bin/python
# @Time ：2023.06.24
# @Author : Xie zy
# @File : common.py
import logging
import os
from datetime import datetime, timezone, timedelta

import requests

CALLBACK_URL = os.environ['CALLBACK_URL']


def batch_send_to_wechat(msg, list_wechat_id):
    for wx_id in list_wechat_id:
        requests.post(url=CALLBACK_URL, json={
            "wxid": wx_id,
            "content": msg
        })


def startLogging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')


def getBJTodayDateStr():
    bj_time_now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    return bj_time_now.strftime('%Y-%m-%d')
