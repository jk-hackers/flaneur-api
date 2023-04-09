# -*- coding: utf-8 -*-
import os
from flask import request
from flask_restful import Resource
import openai
from utils import get_location_news

openai.api_key = os.getenv("OPENAI_API_KEY")


class StoryList(Resource):

    def post(self):
        prompt = request.json["prompt"]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[ 
            {"role": "system", "content": "你是一位见多识广、有教养的优雅女士，你现在正在和一位朋友视频通话，你带着他一起一边散步一边聊天，请你按照我的要求简要介绍周遭环境，可以适当发挥。请你参考 Louis Vuitton SoundWalk 的语言风格，用「我们」作为主语。请注意，不是扮演导游，不要打招呼，不要说欢迎/嗨/嘿/你好，直接开始。不要提到正在打视频电话。当你使用形容词时，不要使用任何表示程度的副词，如”非常””很”。100 字左右。英文输出"} ,
            {"role": "user", "content": prompt}
            ],
            n=2,
            max_tokens=100,
            stream=False,
            temperature=0)
        return {"text": response.choices}

    
