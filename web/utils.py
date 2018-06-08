# -*- coding: utf-8 -*-

import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(BASE_DIR)

from settings import DB_PARAM
from pymongo import MongoClient
from datetime import timedelta


def get_db():
    client = MongoClient(DB_PARAM['ip'], DB_PARAM['port'],
                         username=DB_PARAM['username'],
                         password=DB_PARAM['password'],
                         authSource='future_news', )

    db = client[DB_PARAM['database']]
    return db


def datetime_format(dt):
    dt = dt + timedelta(hours=8)
    return dt.strftime("%Y-%m-%d %H:%M")