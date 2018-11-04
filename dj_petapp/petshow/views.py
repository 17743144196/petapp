from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from . import models
import json
import datetime
import uuid
import jwt
import dj_petapp.settings as settings
from .tests import timebefore

from django.db import connection
from random import randint, sample
# Create your views here.

# 上传照片
def DicLoad(request):
    if request.method == 'POST':
        # return JsonResponse({"code": "408"})
        # try:
        # 此处可以接收文件和字符串
        f1 = request.FILES['usericon']
        # 设置保存的文件名
        name = str(uuid.uuid4()) + "." + f1.name.split('.')[1]
        print(name)
        # print('1111',name)
        fname = '%s/pic/%s' % (settings.STATICFILES_DIRS[0], name)
        # print(fname)
        # 由于文件是二进制流的方式，所有要用chunks()
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        # 驾照背面
        return JsonResponse({"name": name})
        # except Exception as ex:
        #     print(ex)
        return JsonResponse({"code": "407"})
    else:
        return JsonResponse({"code": "408"})
def FlieName(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            p = {
                "photo":'http://127.0.0.1:8000/media/pic/'+  data["photo"],
                "contents":data["contents"],
                "user_id": data["user_id"]
            }
            print(p)
            res = models.show.objects.create(**p)
            return JsonResponse({"code": "808"})
        except Exception as ex:
            # print(ex)
            return JsonResponse({"code": "409"})
    else:
        return JsonResponse({"code": "401"})


# 宠物秀首页
def showp(request,index):
    try:
        pagesize = 10
        index = int(index)
        ty = models.show.objects.all().values("contents","photo","liulan","zan","pinglun","time","user__name","id","user__photo").order_by('-time')[pagesize * (index - 1):pagesize * index]
        print(list(ty))
        for i in ty:
            i["time"] = timebefore(i["time"].replace(tzinfo=None))
        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})

def acount(request,con):
    try:
        if not con:
            len = models.show.objects.all().count()
        else:
            len = models.show.objects.filter(title__regex=con).count()

        return JsonResponse({"acount":len})
    except Exception as ex:
        return JsonResponse({"code": "409"})
# 宠物秀详情页
def showdetail(request,a):
    try:

        old_views = int(models.show.objects.filter(id=a).values("liulan")[0]["liulan"]) + 1
        new = models.show.objects.filter(id=a).update(liulan=old_views)
        ty = models.show.objects.filter(id=a).values("contents","photo","liulan","zan","pinglun","time","user__name","id","user__photo").order_by('-time')
        print(list(ty))
        for i in ty:
            i["time"] = timebefore(i["time"].replace(tzinfo=None))
        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
# 宠物秀详情页评论接收放入数据库
def comments(request):
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
                "show_id": data["show_id"],
            }
            print(d)
            record = models.showcomment.objects.create(**d)
            print(record)
            n = {"code": 200}
            # return JsonResponse({"code":"200"})
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)

  # 显示
def showcomments(request, a):
    try:
        ty = models.showcomment.objects.filter(show_id=a).values("id","content","like","time","show_id","user_id","user__name","user__photo").order_by('-time')
        print(list(ty))
        for i in ty:
            i["time"] = timebefore(i["time"].replace(tzinfo=None))

        return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        # return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})

