from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from . import models
import json
import datetime
from datetime import date
from .tests import timebefore
from django.db import connection
from random import randint, sample
# Create your views here.
def forumtype(request):
    try:
        ty = models.type.objects.all().values('type','id').order_by('id')
        print(list(ty))
        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})

def getforum(request,index,tp):
        try:
            print(tp)
            cursor = connection.cursor()
            index = int(index)
            pagesize = 10
                # con=int(con)
            # tp = int(tp)
            sql = "select title,name,date,type_id,zan,lookers,forum_forum.id from forum_forum INNER JOIN user_user on user_user.id=forum_forum.user_id where type_id like '%{0}%';".format(
                    tp);
            res = cursor.execute(sql);
            print(dir(res))
            row = cursor.fetchall();
            data = []
            for item in row:
                print(item)
                j = {}
                j["title"] = item[0]
                j["name"] = item[1]
                j["date"] = item[2]
                j["type_id"] = item[3]
                j["zan"] = item[4]
                j["lookers"] = item[5]
                j["id"] = item[6]
                data.append(j)
            n = len(data)
            print(n)
            print(index)
            # return HttpResponse(json.dumps(data[pagesize * (index - 1):pagesize * index], ensure_ascii=False))
            return JsonResponse({"data": data[pagesize * (index - 1):pagesize * index], "n": n})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "409"})

def search(request,a):
    try:
        zz = models.forum.objects.filter(id=a).values("user__photo","user__name","date","id","title","picture","content","zan","lookers","contact","phone","weixin","address","type_id","user_id")
        for i in zz:
            i["date"] = timebefore(i["date"].replace(tzinfo=None))
        # return JsonResponse({"name": list(adds)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(zz), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
# 论坛评论
def comment(request):
    if request.method == "POST":
        try:
            n = 0
            data = json.loads(request.body)
            print(data)
            # a=models.adopt.objects.filter(id=data["pet_id"]).values("user_id")[0]['user_id']
            # print(a)
            d = {
                "content": data["content"],
                "user_id": data["user_id"],
                "forum_id": data["forum_id"],
            }
            print(d)
            record = models.forumcomment.objects.create(**d)
            print(record)
            n = {"code": 200}
            # return JsonResponse({"code":"200"})
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)

def forumcomment(request, a):
    try:

        ty = models.forumcomment.objects.filter(forum_id=a).values("user__photo", "user__name", "id", "content", "like",
                                                            "forum_id", "user_id","time")
        # ty = models.forumcomment.objects.filter().values()

        for i in ty:
            i["time"] = timebefore(i["time"].replace(tzinfo=None))
        print(ty[0]["time"])

        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})