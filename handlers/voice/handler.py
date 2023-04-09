# -*- coding: utf-8 -*-
import os
from flask import request
from flask_restful import Resource
from utils import text_to_voice, fetch_voices, upload_file


class TextToVoice(Resource):

    def get(self):
        return fetch_voices()

    def post(self):
        data = request.get_json()
        voice = text_to_voice(data["text"], data["voice"])
        url = upload_file(voice)
        return {"url": url}
    
