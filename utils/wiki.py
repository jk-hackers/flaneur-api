
# -*- coding: utf-8 -*-
import wikipediaapi
from utils.redis import cache

wiki_wiki = wikipediaapi.Wikipedia(language='zh', extract_format=wikipediaapi.ExtractFormat.WIKI)


def fetch_location_from_wiki(name):
    key = "wiki:{}".format(name)
    data = cache.get(key)
    if data:
        return data.decode("utf-8")
    page = wiki_wiki.page(name)
    if not page.exists():
        return ""

    cache.set(key, page.text)
    return page.text
