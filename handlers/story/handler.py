# -*- coding: utf-8 -*-
import os
from flask import request
from flask_restful import Resource
import openai
from utils import get_location_news

openai.api_key = os.getenv("OPENAI_API_KEY")


class StoryList(Resource):

    def gen_message(self, location, weather, geo, news):
        text = '''
        请你参考 Louis Vuitton SoundWalk 的语言风格，用「我们」作为主语。
        请注意，不是扮演导游，不要打招呼，不要说欢迎/嗨/嘿/你好，直接开始。不要提到正在打视频电话。当你使用形容词时，不要使用任何表示程度的副词，如”非常””很”。
        300字左右。

        介绍需要涵盖以下信息：
        - 位置 {location}
        - 天气是 {weather}
        - 你正在坐标 {geo} 附近
        - 有如下新闻 {news}
        '''.format(location=location, weather=weather, geo=geo, news=' \n'.join(news))
        return text
    
    def fetch_news(self, location):
        return []

    def post(self):
        location = request.json["location"]
        weather = request.json["weather"]
        geo = request.json["geo"]
        news = get_location_news(locaiton=location)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[ 
            {"role": "system", "content": "你是一位见多识广、有教养的优雅女士，你现在正在和一位朋友视频通话，你带着他一起一边散步一边聊天，请你按照我的要求简要介绍周遭环境，可以适当发挥。"} ,
            {"role": "user", "content": self.gen_message(location=location, weather=weather, geo=geo, news=news)}
            ],
            n=2,
            stream=False,
            # max_tokens=300,
            temperature=0)
        return {"text": response.choices}

    
