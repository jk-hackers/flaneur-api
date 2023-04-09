# -*- coding: utf-8 -*-
import os
import random
import string
import requests

headers = {
    "xi-api-key": os.getenv("ELEVEN_LABS_API_KEY"),
    "accept": "audio/mpeg"
}


def text_to_voice(text, voice):
    url = "https://api.elevenlabs.io/v1/text-to-speech/{}".format(voice)
    payload = {
      "text": text,
      "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
      }
    }
    response = requests.post(url=url, json=payload, headers=headers)
    return response.content

def fetch_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    response = requests.get(url, headers=headers)
    return response.json()
