# from django.shortcuts import render
# from django.http import HttpResponse, response, JsonResponse
# from . import models
# import json
# import datetime
#
# from django.db import connection
# from random import randint, sample
# # Create your views here.
#
# def xinxi(request):
#     if request.method == "POST":
#         try:
#             n=0
#             data = json.loads(request.body)
#             print(data)
#             a=models.adopt.objects.filter(id=data["pet_id"]).values("user_id")[0]['user_id']
#             print(a)
#             d = {
#                 "name": data["name"],
#                 "telepthone":data["telephone"],
#                 "reason": data["causes"],
#                 "state":'待领养',
#                 "adopt_uer_id_id":a,
#                 "lingyang_user_id_id":data["user_id"]
#
#             }
#             print(d)
#             record = models.lingyang.objects.create(**d)
#             print(record)
#             n = {"code": 200}
#             # return JsonResponse({"code":"200"})
#         except Exception as ex:
#             n = {"code": "500"}  # 程序错误
#             # return JsonResponse({"code": "505"})
#             print(ex)
#         finally:
#             return JsonResponse(n)
#
#
from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from . import models
import json
from user.miaodi import sendIndustrySms
from email.mime.text import MIMEText

import smtplib
from django.db import connection
# from random import randint, sample
# Create your views here.

# 检查邮箱是否存在
def checkemail(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            a = models.user.objects.filter(id=data["id"]).values("email")[0]['email']
            if not a :
                n = {"code": "210" ,"data":"邮箱不存在，请去个人中心填写邮箱"}
            else:
                n={"code":"200"} #邮箱存在

        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)
def xinxi(request):
    if request.method == "POST":
        try:
            n=0
            data = json.loads(request.body)
            # print(data)
            a=models.adopt.objects.filter(id=data["pet_id"]).values("user_id")[0]['user_id']
            adopt_user=models.adopt.objects.filter(id=data["pet_id"]).values("user_id__telephone","user_id__name","user_id__email")
            # print(adopt_user_phone[0]["user_id__telephone"])
            phone=adopt_user[0]["user_id__telephone"]
            name=adopt_user[0]["user_id__name"]
            email = adopt_user[0]["user_id__email"]
            sendEmail(email)
            d = {
                "name": data["name"],
                "telepthone":data["telephone"],
                "reason": data["causes"],
                "state":'待领养',
                "adopt_uer_id_id":data["pet_id"],
                "lingyang_user_id_id":data["user_id"]

            }
            print(d)
            record = models.lingyang.objects.create(**d)
            # print(record)
            n = {"code": 200}
            smsContent = '【宠物驿站平台】亲爱的{0}，有人要领养您的宠物，请前往个人中心查看。回T退订'.format(name)

            sendIndustrySms(phone,smsContent)


            # return JsonResponse({"code":"200"})
        except Exception as ex:
            n = {"code": "500"}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)
# 发送邮箱网址
def sendEmail(email):

    try:
        email = str(email)
        url="www.baidu.com"
        msg = MIMEText(url, 'plain', 'utf-8')  # 用于存放邮件内容
        msg["From"] = "jinzhengwy@163.com"  # 这是来自发件人的邮箱
        msg["To"] = email # 这是接收邮件人的邮箱
        msg["Subject"] = "【我的狗子】验证码为"  # 这是邮件的标题
        print(111111111111111111)
        server = smtplib.SMTP("smtp.163.com", 25)  # qq邮箱 SMTP服务器地址
        # server.set_debuglevel(1)
        server.login(user='jinzhengwy@163.com', password='renhongyang520')
        server.send_message(msg=msg)

        server.close()
        print(2222222222222222222222222)

        c=200
    except Exception as ex:
        print(ex)
        c=300
    finally:
        return c

#显示领养信息
def showlingyang(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # print(data)
            pet_id = data["pet_id"]

            lingyang_user = models.lingyang.objects.filter(adopt_uer_id_id=pet_id).values("reason", "name",
                                                                                          "telepthone",
                                                                                          "lingyang_user_id_id","id","display","state")

            k=[]
            # print(bb)
            for i in lingyang_user:
                print(i)
                lingyang_user_id = i['lingyang_user_id_id']
                cursor = connection.cursor()
                sql = "select * from detailed_address WHERE user_id = {0}".format(int(lingyang_user_id))
                bb = cursor.execute(sql)
                dd = cursor.fetchall()

                if i["display"] == '0':
                    continue

                i["address"]=dd[0][2] + ' ' + dd[0][1] + ' ' + dd[0][3] + ' ' + dd[0][4]
                print(i)
                k.append(i)
            n = {"code": 201,"lingyang_user":k}
            return JsonResponse(n)
        except Exception as ex:
            n = {"code": 500}  # 程序错误
            print(ex)
            return JsonResponse(n)

#领养信息表中的删除操作
def dellingyang(request):
    if request.method == 'POST':
        try:
            id = json.loads(request.body)["id"]

            cursor = connection.cursor()
            sql = "UPDATE lingyang_lingyang set display = 0 WHERE id = {0}".format(id)
            cursor.execute(sql)

            return JsonResponse({"code":"200"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"500"})
    else:
        return JsonResponse({"code":"404"})

# 确认订单
def confirm(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # print(data)
            pet_id=data["pet_id"]
            #获取领养表id
            id = data["num"]
            #获取领养者的id
            cursor = connection.cursor()
            sql = "select lingyang_user_id_id from lingyang_lingyang where id = {0}".format(id)
            cursor.execute(sql)
            d = cursor.fetchone()
            # print(d[0])
            lingyang_id = d[0]


            # lingyang_id=data["lingyang_id"]
            a=models.adopt.objects.filter(id=pet_id).update(state_type_id=2)
            b= models.lingyang.objects.filter(adopt_uer_id=pet_id).values().update(state="被领养")
            c=models.lingyang.objects.filter(lingyang_user_id_id=lingyang_id,adopt_uer_id=pet_id).values().update(state="已领养")
            email = models.user.objects.filter(id=lingyang_id).values()[0]["email"]
            print(email)
            msg = MIMEText("congratulation!! Your adoption request has been accepted!!.", 'plain', 'utf-8')  # 用于存放邮件内容
            msg["From"] = "jinzhengwy@163.com"  # 这是来自发件人的邮箱
            msg["To"] = email  # 这是接收邮件人的邮箱
            msg["Subject"] = "【我的狗子】温馨提示"  # 这是邮件的标题
            print(111111111111111111)
            server = smtplib.SMTP("smtp.163.com", 25)  # qq邮箱 SMTP服务器地址
            # server.set_debuglevel(1)
            server.login(user='jinzhengwy@163.com', password='renhongyang520')
            server.send_message(msg=msg)

            server.close()



            n={"code": 200}
        except Exception as ex:
            n = {"code": 500}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)
# 取消订单
def cancel(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            data = json.loads(request.body)
            # print(data)
            pet_id = data["pet_id"]
            # 获取领养表id
            id = data["num"]
            # 获取领养者的id
            cursor = connection.cursor()
            sql = "select lingyang_user_id_id from lingyang_lingyang where id = {0}".format(id)
            cursor.execute(sql)
            d = cursor.fetchone()
            # print(d[0])
            lingyang_id = d[0]

            c = models.lingyang.objects.filter(lingyang_user_id_id=lingyang_id, adopt_uer_id=pet_id).values().update(
                state="被拒绝")
            email = models.user.objects.filter(id=lingyang_id).values()[0]["email"]
            print(email)

            msg = MIMEText("sorry!! Your adoption request has been rejected.", 'plain', 'utf-8')  # 用于存放邮件内容
            msg["From"] = "jinzhengwy@163.com"  # 这是来自发件人的邮箱
            msg["To"] = email  # 这是接收邮件人的邮箱
            msg["Subject"] = "【我的狗子】温馨提示"  # 这是邮件的标题
            print(111111111111111111)
            server = smtplib.SMTP("smtp.163.com", 25)  # qq邮箱 SMTP服务器地址
            # server.set_debuglevel(1)
            server.login(user='jinzhengwy@163.com', password='renhongyang520')
            server.send_message(msg=msg)

            server.close()
            n = {"code": 200}
        except Exception as ex:
            n = {"code": 500}  # 程序错误
            # return JsonResponse({"code": "505"})
            print(ex)
        finally:
            return JsonResponse(n)


