# -*- coding: utf-8 -*-
import oss2
import os
import hashlib


def upload_file(content):
    auth = oss2.Auth(os.getenv('ALI_OSS_KEY'), os.getenv('ALI_OSS_SECRET'))
    bucket = oss2.Bucket(auth, 'https://oss-accelerate.aliyuncs.com', 'kk-calendar')
    path = "jk-hackathon/{}.mp3".format(_gen_filename(content))
    bucket.put_object(path, content)
    return "https://img2.kroknow.cn/{}".format(path)


def _gen_filename(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()
