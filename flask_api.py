# -*- coding: utf-8 -*-
# @Author  : catnlp
# @FileName: flask_api.py
# @Time    : 2020/9/5 11:55

from flask import Flask
from flask_restful import Resource, Api
from time import sleep

app = Flask(__name__)
api = Api(app)


class Root(Resource):
    def get(self):
        print('睡10秒')
        sleep(10)
        print('醒了')
        return {'message': 'hello'}


api.add_resource(Root, '/')

if __name__ == "__main__":
    app.run()
