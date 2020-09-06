# -*- coding: utf-8 -*-
# @Author  : catnlp
# @FileName: fast_api.py
# @Time    : 2020/9/5 11:57

import uvicorn
from fastapi import FastAPI
from time import sleep

app = FastAPI()


@app.get('/')
def root():
    print('睡10秒')
    sleep(10)
    print('醒了')
    return {'message': 'hello'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
