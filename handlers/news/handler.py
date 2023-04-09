# -*- coding: utf-8 -*-
import os
from flask import request
from flask_restful import Resource
from utils import fetch_news


class News(Resource):
    def get(self):
        location = request.args.get("location")
        news = fetch_news(location)
        return  {"news": news}
