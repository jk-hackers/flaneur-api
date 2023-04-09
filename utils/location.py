# -*- coding: utf-8 -*-

import requests

from utils.google import fetch_location_from_google
from utils.wiki import fetch_location_from_wiki

sites = {
    "BAIKE": 'baike.baidu.com',
    "XHS": "www.xiaohongshu.com",
    "ZH": "www.zhihu.com",
}

def get_location_data(name):
    # 从各种数据源获取地点相关的数据
    data =  {
        'BAIKE': fetch_location_from_google(name, sites['BAIKE']),
        'XHS': fetch_location_from_google(name, sites['XHS']),
        'ZH': fetch_location_from_google(name, sites['ZH']),
        'WIKI': fetch_location_from_wiki(name)
    }
    values = list(data.values())
    return values

def get_location_news(locaiton):
    return []
