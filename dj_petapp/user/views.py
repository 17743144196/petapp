from django.http import JsonResponse
import json
from . import models
import jwt
from datetime import datetime, timedelta
# from ..utils.miaodi import sendIndustrySms
# from ..utils.memcached import *
import random
from .miaodi import sendIndustrySms

from django.db import connection
from datetime import  datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMENonMultipart
from werkzeug.security import generate_password_hash,check_password_hash

# from MyProject.static.util_token import *
# Create your views here.
def login(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            if data["telephone"] and data["password"] and data["telephone"].isdigit() and data["password"].isalnum():
                d = models.user.objects.get(telephone=data["telephone"])
                if check_password_hash(d.password,data["password"]):
                    datetimeInt = datetime.utcnow() + timedelta(seconds=1200)
                    SECRET_KEY = "123456"
                    option = {
                        "iss": "jinzhengjun",
                        "exp": datetimeInt,
                        "aud": "webkit",
                        "user_id": {"telephone": json.loads(request.body)['telephone']}
                    }
                    token = jwt.encode(option, SECRET_KEY, "HS256")
                    global resp
                    resp = {"code": "200"}
                    resp = JsonResponse({"code": "201","user_id":d.id,"tel":json.loads(request.body)['telephone']})
                    resp['token'] = token
                    resp["Access-Control-Expose-Headers"] = "token"
                else:
                    resp = JsonResponse({"code": "403"})
            else:
                resp = JsonResponse({"code": "402"})
        except Exception as ex:
            print(ex)
            resp = JsonResponse({"code": "401"})
        finally:
            return resp

def register(request):
    if request.method == "POST":
        n = 0
        data = json.loads(request.body)
        print(data)
        try:
            data = json.loads(request.body)
            print(data)
            cursor = connection.cursor()
            sql = "select * from securty WHERE telephone = {0}".format(data["telephone"])
            bb = cursor.execute(sql)
            dd = cursor.fetchone()
            print(dd)
            print(dd[3])
            if dd[3] == 2:
                if data["telephone"] and data["password"] and data["npassword"] and data["password"] == data["npassword"]:
                    d = {
                        "telephone": data["telephone"],
                        "password": generate_password_hash(data["password"],method='pbkdf2:sha1:2000',salt_length=6),
                        "name":data["name"]

                    }
                    record = models.user.objects.create(**d)
                    # print(record)
                    n = {"code": 200}
                else:
                    n = {"code": "403"}  #账号或密码错误
            else:
                n = {"code":"406"}  #没有验证码

        except Exception as ex:
            n = {"code": "500"}   #程序错误
            print(ex)
        finally:
            return JsonResponse(n)

def sendcode(request):
    '''
    :param          mobile
    :return:        (1): code:412       手机号码输入不正确，或者已被注册
                    (2): code:200       发送短信成功
    '''


    # print(now_date + 60)
    #
    # timeArray = time.localtime(now_date)
    #
    # otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    #
    # print(otherStyleTime)

    if request.method == "POST":
        mobble = json.loads(request.body)
        mobble=int(mobble['phone'])
        print(mobble)#验证表单
        # if form.validate():
        #
        code=random.randrange(1000,9999)
        code=str(code)
        print(code)
        # smsContent='【宠物驿站平台】您的验证码为{1}，请于{2}分钟内正确输入，如非本人操作，请忽略此短信。'.format(0,code,5)
        # sendIndustrySms(mobble,smsContent)
        # sendIndustrySms(mobble,smsContent)


        # #将获取到的验证码存储到数据库中
        now_date = time.time() + 120;

        cursor = connection.cursor()

        sql = "DELETE from securty WHERE telephone = {0}".format(mobble)

        n = cursor.execute(sql)

        sql = "insert into securty() VALUE({0},{1},{2},{3})".format(mobble,code,now_date,1)

        bb = cursor.execute(sql)


        return JsonResponse({'code': 200, 'message': '发送成功'})
        # else:
        #     message = form.errors.popitem()[1][0]                 #弹出第一条验证失败错误信息
        #     print(type(jsonify({'code':406})))
        #     return JsonResponse({'code':412,'message':message})
        # response=JsonResponse({'code':200,'message':'发送成功'})
        # response['Access-Control-Allow-Origin']='*'


def yezheng(request):

    now_dates = time.time()

    mobble = json.loads(request.body)

    mobbl = int(mobble['phone'])
    yecode = int(mobble["yecode"])

    try:
        cursor = connection.cursor()

        sql = "select * from securty WHERE telephone = {0}".format(mobbl)

        bb = cursor.execute(sql)

        res = cursor.fetchone()


        if (res[1] == yecode) and (float(res[2]) >= now_dates):

            sql = "UPDATE securty set state = 2 WHERE telephone = {0}".format(mobbl)
            bb = cursor.execute(sql)
            r = {"code":200}
        else:
            r = {"code":403}

        return JsonResponse(r)

    except Exception as ex:
        print(ex)

def getNameImg(request):
    if request.method == "POST":
        try:
            id = json.loads(request.body)["id"]

            cursor = connection.cursor()

            sql = "select name,photo from user_user WHERE id = {0}".format(id)

            r = cursor.execute(sql)
            if r == 0:
                return JsonResponse({"code":"405"})
            else:
                d = cursor.fetchone()

                dd = {
                    "name":d[0],
                    "photo":str(d[1]),
                }
                return JsonResponse(dd)
        except Exception as ex:
            return JsonResponse({"code":"403"})

#绑定邮箱
def addemail(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # print(1111111111)
            # print(data)
            models.user.objects.filter(id=data["user_id"]).update(email=data["email"])
            resp = {"code": "200"}
        # try:
        #     pass
            # data = json.loads(request.body)
            # if data["telephone"] and data["password"] and data["telephone"].isdigit() and data["password"].isalnum():
            #     d = models.user.objects.get(telephone=data["telephone"])
            #     if check_password_hash(d.password,data["password"]):
            #         datetimeInt = datetime.now() + timedelta(seconds=240)
            #         SECRET_KEY = "123456"
            #         option = {
            #             "iss": "jinzhengjun",
            #             "exp": datetimeInt,
            #             "aud": "webkit",
            #             "user_id": {"telephone": json.loads(request.body)['telephone']}
            #         }
            #         token = jwt.encode(option, SECRET_KEY, "HS256")
            #         global resp
            #         resp = {"code": "200"}
            #         resp = JsonResponse({"code": "201","user_id":d.id})
            #         resp['token'] = token
            #         resp["Access-Control-Expose-Headers"] = "token"
            #     else:
            #         resp = JsonResponse({"code": "403"})
            # else:
            #     resp = JsonResponse({"code": "402"})
        except Exception as ex:
            print(ex)
            resp= {"code": "401"}

        finally:
            # return resp
            return  JsonResponse(resp)

# 发送邮箱验证码
def sendEmail(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = str(data['email'])
            print(email)
            code = str(random.randrange(1000, 9999))
            print(code)
            msg = MIMEText(code, 'plain', 'utf-8')  # 用于存放邮件内容
            msg["From"] = "jinzhengwy@163.com"  # 这是来自发件人的邮箱
            msg["To"] = email # 这是接收邮件人的邮箱
            msg["Subject"] = "【我的狗子】验证码为"  # 这是邮件的标题
            print(111111111111111111)
            server = smtplib.SMTP("smtp.163.com", 25)  # qq邮箱 SMTP服务器地址
            # server.set_debuglevel(1)
            server.login(user='jinzhengwy@163.com', password='renhongyang520')
            server.send_message(msg=msg)

            server.close()

            now_date = time.time() + 120;

            cursor = connection.cursor()


            sql = "DELETE from emailcode WHERE email = '{0}'".format(email)
            n = cursor.execute(sql)

            sql = "insert into emailcode() VALUE ('{0}',{1},{2},{3})".format(email, code, now_date, 1)

            bb = cursor.execute(sql)
            c={"code": "200","codes":code}
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "502"})
        finally:
            return JsonResponse(c)

# 验证邮箱验证码
def yanzhengemail(request):

    now_dates = time.time()

    data = json.loads(request.body)

    email = data['email']
    code = int(data["codes"])

    print(code)
    try:
        cursor = connection.cursor()

        sql = "select * from emailcode WHERE email = '{0}'".format(email)

        bb = cursor.execute(sql)

        res = cursor.fetchone()

        if (int(res[1]) == code) and (float(res[2]) >= now_dates):

            sql = "UPDATE emailcode set state = 2 WHERE email = '{0}'".format(email)
            bb = cursor.execute(sql)
            r = {"code":200}
        else:
            r = {"code":403}

        return JsonResponse(r)

    except Exception as ex:
        print(ex)

def chackphone(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            a = models.user.objects.filter(telephone=data["telephone"]).values()
            print(len(a))

            if len(a)>=1:
                n={"code":200}  #该手机号已存在
            else:
                n={"code": 202}#手机号不存在

        except Exception as ex:
            n ={"code": "500"}   #程序错误
            print(ex)
        finally:
            return JsonResponse(n)

def realname(request):
    if request.method == "POST":
        try:
            n=0
            data = json.loads(request.body)
            d = {
                "name": data["name"],
                "leixing":data["type"],
                "idcard": data["num"],
                "bankcard": data["banknumber"],
                "telephone": data["tel"],
                "user_id": data["user_id"],

            }
            print(d)
            record = models.userbasic.objects.create(**d)
            # print(record)
            n = {"code": 200}
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)

def repassword(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            phone=data["phone"]
            newpassword=data["newpassword"]
            models.user.objects.filter(telephone=phone).values().update(password=generate_password_hash(newpassword,method='pbkdf2:sha1:2000',salt_length=6))

            n={"code":808}
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            print(ex)
        finally:
            return JsonResponse(n)


