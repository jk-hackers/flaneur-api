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
    # https://serpapi.com/users/welcome
    search = GoogleSearch({
            "api_key": os.getenv('SERP_API'),
            "engine": "google",  
            "q": name,
            "tbm": "nws"
        })
    news =  search.get_dict()["news_results"]
    return news