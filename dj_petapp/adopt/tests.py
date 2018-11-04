from django.test import TestCase

from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse

import json
import datetime
import time
from django.db import connection
from random import randint, sample


def timebefore(d):
    chunks = (
        (60 * 60 * 24 * 365, u'年'),
        (60 * 60 * 24 * 30, u'月'),
        (60 * 60 * 24 * 7, u'周'),
        (60 * 60 * 24, u'天'),
        (60 * 60, u'小时'),
        (60, u'分钟'),
    )
    # 如果不是datetime类型转换后与datetime比较


    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    now = datetime.datetime.now()
    delta = now - d
    # 忽略毫秒
    before = delta.days * 24 * 60 * 60 + delta.seconds  # python2.7直接调用 delta.total_seconds()
    # 刚刚过去的1分钟
    if before <= 60:
        return u'刚刚'
    for seconds, unit in chunks:
        count = before // seconds
        if count != 0:
            break
    return json.dumps(count) + unit + u"前"
