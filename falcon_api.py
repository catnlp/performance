# -*- coding: utf-8 -*-
# @Author  : catnlp
# @FileName: flask_api.py
# @Time    : 2020/9/5 11:55

import falcon
from time import sleep
from json import dumps


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        # resp.status = falcon.HTTP_200  # This is the default status
        # print('睡10秒')
        # sleep(10)
        # print('醒了')
        resp.body = dumps({'message': 'hello'})

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', things)
