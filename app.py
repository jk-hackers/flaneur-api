# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

## setup env from .env file
load_dotenv()

from flask import Flask
from flask_restful import Api
from routers import setup_routers

app = Flask(__name__)
api = Api(app)


# setup routers
setup_routers(api=api)


# run app
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"), host="0.0.0.0")