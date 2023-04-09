# -*- coding: utf-8 -*-
from flask_restful import Api

# Import all handlers 
from handlers import *


def setup_routers(api: Api):  
  # Actually setup the Api Resource routing here
  api.add_resource(StoryList, "/story")
  
  api.add_resource(TextToVoice, "/voices")

  api.add_resource(LookupLocation, "/lookup")
  api.add_resource(Weather, "/weather")

