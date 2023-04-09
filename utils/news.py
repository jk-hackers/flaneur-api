# -*- coding: utf-8 -*-
from datetime import date
import os
import json
from serpapi import GoogleSearch
from bs4 import BeautifulSoup

from utils.redis import cache

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}


def fetch_news(name):
    # 获取 link
    key = "news:{}:{}:v1".format(name, date.today())
    data = cache.get(key)
    if data:
        return json.loads(data)

    # https://serpapi.com/users/welcome
    search = GoogleSearch({
            "api_key": os.getenv('SERP_API'),
            "engine": "google",  
            "q": name,
            "tbm": "nws"
        })
    news =  search.get_dict()["news_results"]
    cache.set(key,  json.dumps(news))
    return news