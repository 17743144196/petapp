from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from . import models
import json
import datetime
from datetime import date
import uuid
import jwt
import dj_petapp.settings as settings
from .tests import timebefore

from django.db import connection
from random import randint, sample

SECRET_KEY = "123456"


# Create your views here.
# 添加
def add(request):
    job = {
    }
    if request.method == 'POST':
        try:
            with open('pet_type.json', 'r+', encoding='utf-8') as fp:
                p = json.load(fp)
                print(p[0])
                for i in range(len(p)):
                    print(i)
                    res = models.pettype.objects.create(**p[i])
            return JsonResponse({"code": "808"})
        except Exception as ex:
            # print(ex)
            return JsonResponse({"code": "408"})
# 右侧领养循环
def randadopt(request):
    try:
        a = []
        count = models.adopt.objects.all().count()
        rand_ids = sample(range(53, 53+count), 1)
        print(rand_ids)
        # return JsonResponse({"code": "808"})
        for i in range(len(rand_ids)):
            print(i)

            ty = models.adopt.objects.filter(id=rand_ids[i]).values("title", "picone", "introduce", "id")[0]
            a.append(ty)
            print(ty)

        # ty=list(models.adopt.objects.filter().values("title","user__name","user__photo","onlooker","introduce","date","id","picone","pictwo"))
        # print(ty)
        return HttpResponse(json.dumps(a, ensure_ascii=False))
        # return JsonResponse({"code": "808"})

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
# 宠物类型查询
def pettype(request):
    try:
        ty = models.pettype.objects.all().values('type', 'id').order_by('id')
        print(list(ty))
        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
# 查询省
def search(request):
    try:
        adds = models.province.objects.all().values('name', 'pycode')
        print(list(adds))
        # return JsonResponse({"name": list(adds)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(adds), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
    # 宠物分类
# 领养详情信息通过id查找
def adopts(request, iid):
    try:
        # ty=models.photo.objects.filter(pet_id=iid).values("pet__title","pet__state_type__type","pet__id","pet__provid__name","pet__pet_type__type","pet__pet_sex__sex","pet__isFree","pet__price","pet__onlooker","pet__like","pet__com_num","pet__share","pet__introduce","pet__require","pic_name","pet__user__name")


        old_views=int(models.adopt.objects.filter(id=iid).values("onlooker")[0]["onlooker"])+1
        a = len(models.adopt.objects.get(id=iid).zan_set.all())
        b = len(models.adopt.objects.get(id=iid).comment_set.all())
        new = models.adopt.objects.filter(id=iid).update(onlooker=old_views, like=a, com_num=b)

        # new = models.adopt.objects.filter(id=iid).update(onlooker=old_views, like=a)
        print(models.adopt.objects.filter(id=iid).values("onlooker"))
        ty = models.adopt.objects.filter(id=iid).values("title", "state_type__type", "id", "provid__name",
                                                        "pet_type__type", "pet_sex__sex", "isFree", "price", "onlooker",
                                                        "like", "com_num", "share", "introduce", "yaoqiu", "picone",
                                                        "pictwo", "user__name", "user__id")
        # ty=models.adopt.objects.filter(id=iid).values("title")

        # print(list(ty))
        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
# 领养页面列表
def getpets(request, index, con, tp):
    try:
        cursor = connection.cursor()
        index = int(index)
        pagesize = 10
        if tp:
            # con=int(con)
            tp = int(tp)
            sql = "select picone,title,photo,adopt_adopt.id as id,name,date,onlooker,introduce,pet_type_id,provid_id from adopt_adopt INNER JOIN user_user on adopt_adopt.user_id=user_user.id where provid_id like'%{0}%' and pet_type_id ='{1}' order by date DESC;".format(
                con, tp);
            res = cursor.execute(sql);
            print(dir(res))
            row = cursor.fetchall();
            data = []
            for item in row:
                print(item)
                j = {}
                # 宠物照片
                j["picone"] = item[0]
                # 标题
                j["title"] = item[1]
                # 头像
                j["photo"] = item[2]
                # 宠物id
                j["id"] = item[3]
                # 发布人昵称
                j["name"] = item[4]
                j["date"] = timebefore(item[5].replace(tzinfo=None))
                j["onlooker"] = item[6]
                j["introduce"] = item[7]
                j["pet_type_id"] = item[8]
                j["provid_id"] = item[9]
                data.append(j)

            n = len(data)
            print(n)

        else:
            sql = "select picone,title,photo,adopt_adopt.id as id,name,date,onlooker,introduce,pet_type_id,provid_id from adopt_adopt INNER JOIN user_user on adopt_adopt.user_id=user_user.id where provid_id like '%{0}%' and pet_type_id like'%{1}%' order by date DESC;".format(
                con, tp);

            res = cursor.execute(sql);
            print(dir(res))
            row = cursor.fetchall();
            data = []
            for item in row:
                print(item)
                j = {}
                # 宠物照片
                j["picone"] = item[0]
                # 标题
                j["title"] = item[1]
                # 头像
                j["photo"] = item[2]
                # 宠物id
                j["id"] = item[3]
                # 发布人昵称
                j["name"] = item[4]
                j["date"] = timebefore(item[5].replace(tzinfo=None))
                j["onlooker"] = item[6]
                j["introduce"] = item[7]
                j["pet_type_id"] = item[8]
                j["provid_id"] = item[9]
                data.append(j)

            n = len(data)
            print(n)

        # return HttpResponse(json.dumps(data[pagesize * (index - 1):pagesize * index], ensure_ascii=False))
        return JsonResponse({"data": data[pagesize * (index - 1):pagesize * index], "n": n})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "409"})
# 首页领养
def adoptpp(request, index, con):
    try:
        pagesize = 10

        # 注意类型转化
        index = int(index)
        if con:
            ty = models.adopt.objects.filter(title__regex=con).values("title", "provid__name","user__name","date", "user__photo", "onlooker", "introduce", "id", "picone", "pictwo")[pagesize * (index - 1):pagesize * index]
            for i in ty:
                i["date"] = timebefore(i["date"].replace(tzinfo=None))
        else:
            ty = models.adopt.objects.all().values("title","provid__name", "user__name", "date","user__photo", "onlooker", "introduce", "id", "picone", "pictwo").order_by('-date')[pagesize * (index - 1):pagesize * index]
            for i in ty:
                i["date"] = timebefore(i["date"].replace(tzinfo=None))
            return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
def acount(request,con):
    try:
        if not con:
            len = models.adopt.objects.all().count()
        else:
            len = models.adopt.objects.filter(title__icontains=con).count()
        print(len)
        return JsonResponse({"acount":len})
    except Exception as ex:
        return JsonResponse({"code": "409"})
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
                "pet_id": data["pet_id"],
            }
            print(d)
            record = models.comment.objects.create(**d)
            print(record)
            n = {"code": 200}
            # return JsonResponse({"code":"200"})
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)

    # if request.method == "POST":
    #     resp = {"code": "402"}
    #     try:
    #         data = json.loads(request.body)
    #         print(data["pet"], data["user"], data["content"])
    #
    #         com = {
    #             "pet_id": int(data["pet"]),
    #             "user_id": int(data["user"]),
    #             "content": data["content"]
    #         }
    #
    #         models.comment.objects.create(**com)
    #
    #         resp = JsonResponse({"code": "201"})
    #
    #     except Exception as ex:
    #         print(ex)
    #         resp = JsonResponse({"code": "401"})
    #     finally:
    #         return resp
# 显示评论
def showcomment(request, a):
    try:
        # ty = models.comment.objects.filter(pet_id=a).values("user_id__photo", "user_id__name","id", "content", "time", "like", "pet_id", "user_id")
        ty = models.comment.objects.filter(pet_id=a).values("user_id__photo", "user_id__name", "id", "content", "like",
                                                            "pet_id", "user_id","time")
        for i in ty:
            i["time"] = timebefore(i["time"].replace(tzinfo=None))
        print(ty[0]["time"])

        # return JsonResponse({"name": list(ty)}, json_dumps_params={'ensure_ascii': False})
        return HttpResponse(json.dumps(list(ty), ensure_ascii=False))

    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "408"})
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
# 获取照片名字 # 寄养信息 的
def FlieName(request):
    if request.method == 'POST':

        # try:
        # token = request.META.get('HTTP_TOKEN')
        # print("=====================",token)
        try:

  # tokenMsg = jwt.decode(str(token).encode(), SECRET_KEY, audience='webkit', algorithms=['HS256'])
            data = json.loads(request.body)
            # telephpne = tokenMsg['user_id']
            # Positive = data['Positive']
            # otherSide = data['otherSide']
            # id1 = models.UserBase.objects.filter(telephone=telephpne).values('id')
            # id = list(id1)[0]['id']
            p = {
                "title": data["title"],
                "introduce": data["introduce"],
                "yaoqiu": data["yaoqiu"],
                "pet_type_id": data["pet_type_id"],
                "pet_sex_id": data["pet_sex_id"],
                "isFree": data["isFree"],
                "price": data["price"],
                "provid_id": data["provid_id"],
                "citys": data["citys"],
                "areas": data["areas"],
                "contact": data["contact"],
                "phone": data["phone"],
                "weixin": data["weixin"],
                "qq": data["qq"],
                "user_id": data["user_id"],
                "picone": 'http://127.0.0.1:8000/media/pic/'+ data['Positive'],
                "pictwo": 'http://127.0.0.1:8000/media/pic/'+ data['otherSide'],
                "stat_time": data["stat_time"],
                "end_time": data["end_time"]
                # "picone":data["picone"],
                # "pictwo":data["pictwo"]
            }
            print(p)

            # data1 = {
            #     "picone":Positive,
            #     "pictwo":otherSide,
            #     # "driver_id":id
            # }
            res = models.adopt.objects.create(**p)
            # print('000000',id)
            # print(2222222,Positive)
            # print(3333333, otherSide)
            # n = {"code": 200}
            return JsonResponse({"code": "808"})
        except Exception as ex:
            # print(ex)
            return JsonResponse({"code": "409"})
    else:
        return JsonResponse({"code": "401"})

        # telphone = jwtDecoding(token.encode())['some']


# 插入删除点赞
def dianzan(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            a=models.zan.objects.filter(user_id=data["user_id"],pet_id=data["pet_id"])
            print(a)
            if a:
            #     models.zan.objects.create(**data)
                # print(record)
                a.delete()
                n = {"code": 200}
                # return JsonResponse({"code":"200"})
            else:
                models.zan.objects.create(**data)
                n = {"code": 200}
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)
