# -*- coding: utf-8 -*-

import redis
import os

cache = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=os.getenv("REDIS_PORT", 6379), db=os.getenv("REDIS_DB", 0))