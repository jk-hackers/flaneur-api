# -*- coding: utf-8 -*-
import os
from flask import request
from flask_restful import Resource
from utils import lookup_location, get_weather


class LookupLocation(Resource):

    def get(self):
        geo = request.args.get("geo")
        return lookup_location(geo)


class Weather(Resource):

    def get(self):
        location = request.args.get("location")
        return get_weather(location)
