#!/usr/bin/python
# @Time ：2023.06.24
# @Author : Xie zy
# @File : weather_report.py
import logging
import os
from datetime import time, datetime, timezone, timedelta
import time
import requests
from lxml import etree

# CALLBACK_URL = os.environ['CALLBACK_URL']
# # specific
# GAODE_API_KEY = os.environ['WEATHER_REPORT__GAODE_API_KEY']
# WeChat_ID_LIST = os.environ['WEATHER_REPORT__WeChat_ID_LIST']

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

# 协调世界时
utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
# 北京时间
beijing_now = utc_now.astimezone(SHA_TZ)
TODAY = beijing_now.strftime('%Y-%m-%d %H:%M:%S')
YESTERDAY = (beijing_now.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

# CN时间获取
# BJ_TIME_NOW = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
# TODAY = BJ_TIME_NOW.strftime('%Y-%m-%d')
# YESTERDAY = (BJ_TIME_NOW.now() - timedelta(days=1)).strftime('%Y-%m-%d')


# def send_to_wechat(msg):
#     for wx_id in WeChat_ID_LIST:
#         requests.post(url=CALLBACK_URL, json={
#             "wxid": wx_id,
#             "content": msg
#         })


###############################################################################
# 执行
###############################################################################
# 设置log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

logging.info(beijing_now)
logging.info(beijing_now.tzname())
logging.info("today:" + TODAY)
logging.info("yesterday:" + YESTERDAY)

logging.info('-=--------------------')
BJ_TIME_NOW = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
TODAY = BJ_TIME_NOW.strftime('%Y-%m-%d %H:%M:%S')
YESTERDAY = (BJ_TIME_NOW.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
logging.info("today:" + TODAY)
logging.info("yesterday:" + YESTERDAY)

# for key in FETCH_LIST.keys():
#     # get meta-info
#     name = FETCH_LIST[key]['name']
#     url = FETCH_LIST[key]['url']
#     title_keywords = FETCH_LIST[key].get('title_keywords', [])
#
#     # crawler
#     try:
#         list_articles = fetch_one_module(url, title_keywords)
#     except Exception as e:
#         logging.info(name + "板块 crawler error")
#         send_to_wechat('{date} {module_name} 爬取失败, 请稍后手动重试~'.format(date=YESTERDAY, module_name=name))
#
#     # build msg
#     msg = build_msg_for_one_module(list_articles, name, title_keywords)
#
#     # send to wechat
#     try:
#         send_to_wechat(msg)
#     except Exception as e:
#         logging.info(name + "板块 callback error")
#
#     logging.info(name + "板块 callback success")
#
# '''
# // TODO
# '''
# res = []
#     last_flag = False
#     cookie = COOKIE_TEMP.format(username=USERNAME, password_session=PASSWORD_SESSION)
#     session = requests.Session()
#     params = {
#         "_uid": USERNAME,
#         "p": str(page_num)
#     }
#     headers = {
#         "User-Agent": USER_AGENT,
#         "cookie": cookie,
#         "x-requested-with": "XMLHttpRequest"
#     }
#     response = session.get(url=url, headers=headers, params=params)
#     html = etree.HTML(response.text)
#     len_trs = len(html.xpath('/html/body/div[3]/table/tbody//tr'))
#     for i in range(len_trs):
#         num = str(i + 1)
#         base_url = "https://bbs.byr.cn"
#         link = base_url + html.xpath('/html/body/div[3]/table/tbody/tr[' + num + ']/td[2]/a/@href')[0]
#         title = html.xpath('/html/body/div[3]/table/tbody/tr[' + num + ']/td[2]/a/text()')[0]
#         create_date = html.xpath('/html/body/div[3]/table/tbody/tr[' + num + ']/td[3]/text()')[0]
#         update_date = html.xpath('/html/body/div[3]/table/tbody/tr[' + num + ']/td[6]/a/text()')[0]
#         # 爬取范围：update_time为今天或昨天或第一页的帖子，每天9～10点爬
#         # 选择：create_time为昨天的帖子
#         # 注意：当天的帖子时间为'%H:%M:%S '，否则为'%Y-%m-%d'
#         try:
#             time.strptime(create_date, "%Y-%m-%d")
#         except Exception as e:
#             create_date = TODAY
#         try:
#             time.strptime(update_date, "%Y-%m-%d")
#         except Exception as e:
#             update_date = TODAY
#
#         if page_num != 1 and update_date != TODAY and update_date != YESTERDAY:
#             last_flag = True
#
#         if create_date == YESTERDAY and is_hit_keyword(title, title_keywords):
#             dic = {'title': title, 'link': link}
#             res.append(dic)
