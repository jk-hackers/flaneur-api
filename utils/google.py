# -*- coding: utf-8 -*-
import requests
import os
import json
from serpapi import GoogleSearch
from bs4 import BeautifulSoup

from utils.redis import cache

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

def fetch_location_from_google(name, site):
    content = []
    for link in _get_link(name, site):
        content.append(_fetch_link_content(link))
    return ''.join(content)

def _get_link(name, site):
    # 获取 link
    key = "baikelink:{}:site:{}".format(name, site)
    data = cache.get(key)
    if data:
        return json.loads(data)

    # https://serpapi.com/users/welcome
    search = GoogleSearch({
            "q": name  + " site:" + site, 
            "location": "China",
            "api_key": os.getenv('SERP_API', "e221c21d8e89f1789cfad952531f43df63bf828ae9f543fe7d071591cf692e0f")
        })
    urls = []
    for link in  search.get_dict()['organic_results']:
        urls.append(link['link'])
    
    cache.set(key,  json.dumps(urls))
    return urls

def _fetch_link_content(link):
    key = "baikelink:{}:content".format(link)
    data = cache.get(key)
    if data:
        return data.decode("utf-8")
    
    content = requests.get(link, headers=headers).text
    text = BeautifulSoup(content).get_text()

    cache.set(key,  text)
    return text

