from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
import uuid
import random
import dj_petapp.settings as settings
from qiniu import  Auth,put_file,etag
from django.db import connection
from .miaodi import sendIndustrySms
import time
import jwt
from datetime import datetime,timedelta
from werkzeug.security import generate_password_hash,check_password_hash
import qiniu.config

# Create your views here.

def index(request):
    return JsonResponse({"code":"index"})

def personal(request):
    if request.method == 'GET':
        return HttpResponse("file:///C:/Users/%E9%87%91%E6%AD%A3%E5%86%9B/Desktop/myproject/sign_in.html")

def safety(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse({"code":"200"})
    else:
        return JsonResponse({"code":"404"})


#在后台中存储图片
def upload(request):
   if request.method == "POST":
       try:
           #获取文件或图片
           file = request.FILES["usericon"]
           # print(request.FILES["usericon"].size)
           # print(request.FILES["usericon"].name)

           #利用uuid产生一个唯一名称
           filename = str(uuid.uuid4()) + "." + file.name.split(".")[1]

           #设置保存文件的路径
           fname = '{0}/pic/{1}'.format(settings.MEDIT_ROOT,filename)

            #将文件保存到指定的路径种
           with open(fname,"wb+") as fp:
               #设置缓存池
              for c in file.chunks():
                  fp.write(c)
           print(fname)
           return JsonResponse({"code":"200"})
       except Exception as ex:
           print("11111111111")
           return JsonResponse({"code":"409"})

#将图片上传到第三方软件种
def qiniu(request):
  if request.method == 'GET':
      try:

          # 填写七牛云的密钥
          access_key = "PfBG3HayGCpokh-sp1KD2cnVCjJpWmqY5LQWV7QG"
          secret_key = "6_PuVQscFj2QB1R5-ZgSmwQH8MUT7IQE2LyOtz7X"

          # 构建健全对象
          q = Auth(access_key, secret_key)
          file = request.GET.get("key")
          print(file)
          # 要上传的空间
          bucket_name = "petapp"

          # 上传到七牛后保存的文件名
          key = str(uuid.uuid4()) + "." + file.split(".")[1]

          # 生成上传的TOKEN,可以指定过期时间
          token = q.upload_token(bucket_name, key, 3600)
          return JsonResponse({"token": token, "filename": key})

      except Exception as ex:
          print(ex)
          return JsonResponse({"code": "409"})

#将上传的文件名存储到数据库中
def uploadimg(request):
    if request.method == "POST":
        data = json.loads(request.body)
        imgName = data["imagsname"]
        tel = data["telephone"]
        try:
            cursor = connection.cursor()
            sql = "UPDATE user_user set photo = '{0}' WHERE telephone = {1}".format(imgName,tel)
            r = cursor.execute(sql)

            if r == 1:
                return JsonResponse({"code":"200"})
            else:
                return JsonResponse({"code": "401"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"403"})


#获取个人基本信息接口
def getInformation(request):
    if request.method == 'POST':
        try:
            token = json.loads(request.body)["token"]
            c = get_token(token)

            if c == 406:
                return JsonResponse({"code":"406"})

            tel = json.loads(request.body)["telephone"]
            cursor = connection.cursor()

            # 获取用户的基本信息
            sql = "select u.telephone,u.photo,u.name,u.birthday,u.email,u.id from user_user as u where telephone = {0}".format(tel)
            res = cursor.execute(sql)
            data = cursor.fetchone();

            #获取用户的地址信息
            sql = "select d.city_name,d.province_name,d.area,d.address_discribe from user_user as u,detailed_address as d WHERE d.user_id = {0}".format(data[-1])
            res = cursor.execute(sql)
            d = cursor.fetchone();

            print(data)
            if(res):
                datas = {}
                datas["telephone"] = data[0]
                datas["photo"] = data[1]
                datas["name"] = data[2]
                datas["datetime"] = data[3]
                datas["province"] = d[0]
                datas["city"] = d[1]
                datas["area"] = d[2]
                datas["addressDiscribe"] = d[3]
                datas["email"] = data[4]
            else:
                datas = {}
                datas["telephone"] = data[0]
                datas["photo"] = data[1]
                datas["name"] = data[2]
                datas["datetime"] = data[3]
                datas["province"] = ""
                datas["city"] = ""
                datas["area"] = ""
                datas["addressDiscribe"] = ""
                datas["email"] = data[4]


            return JsonResponse({"code": "200","datas":datas})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"401"})

#修改登入密码
def alterp(request):
    if request.method == 'POST':
        #验证token
        token = json.loads(request.body)["token"]
        c = get_token(token)

        if c == 406:
            return JsonResponse({"code": "406"})

        data = json.loads(request.body)
        print(data)
        tel = data["telephone"]
        newp = data["password"]
        nnewp = data["npassword"]
        # print("11111111")
        #获取验证码的状态
        cursor = connection.cursor()
        sql = "select * from securty WHERE telephone = {0}".format(tel)
        bb = cursor.execute(sql)
        dd = cursor.fetchone()
        codes = dd[3]

        if newp and nnewp and newp == nnewp and codes == 2:

            #利用sql语句直接存储新密码
            cursor = connection.cursor()
            newp = generate_password_hash(newp,method='pbkdf2:sha1:2000',salt_length=6),

            #这里出现了问题，sql能直接存储加盐密码 应为加盐后对象是list类型要提出来
            sql = "UPDATE user_user set `password` = '{0}' where telephone = {1}".format(newp[0],tel)
            r = cursor.execute(sql)

            return JsonResponse({"code":"200"})

#获取短信验证
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
        # smsContent='【宠物驿站平台】您的验证码为{0}，请于{1}分钟内正确输入，如非本人操作，请忽略此短信。'.format(code,5)
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

#存储用户的生日和住址到数据库中
#获取省份
def getProvince(request):
    if request.method == 'POST':
       cursor = connection.cursor();
       sql = "SELECT address_name,address_id from ops_address where address_type = 1"
       cursor.execute(sql)
       d = cursor.fetchall();
       p = []
       for item in d:
           j = {}
           j["province"] = item[0]
           j["addressId"] = item[1]
           p.append(j)
       return JsonResponse({"code":"200","p":p})

#获取市
def getCity(request):
    if request.method == 'POST':
        print(json.loads(request.body))
        pId = json.loads(request.body)["Province"]
        cursor = connection.cursor();
        sql = "select address_name,address_id from ops_address WHERE province_id = {0} and address_type = 2".format(pId)
        cursor.execute(sql)
        d = cursor.fetchall();
        p = []
        for item in d:
            j = {}
            j["city"] = item[0]
            j["addressId"] = item[1]
            p.append(j)
            print(p)
        return JsonResponse({"code": "200", "p": p})

#获取区地址信息
def getAare(request):
    if request.method == 'POST':
        print(json.loads(request.body))
        pId = json.loads(request.body)["cityid"]
        cursor = connection.cursor();
        sql = "select address_name,address_id from ops_address WHERE address_parent_id = {0}".format(pId)
        cursor.execute(sql)
        d = cursor.fetchall();
        p = []
        for item in d:
            j = {}
            j["area"] = item[0]
            j["addressId"] = item[1]
            p.append(j)
            print(p)
        return JsonResponse({"code": "200", "p": p})

#存储个人中心上传的生日和地址
def savasd(request):
    if request.method == 'POST':
        d = json.loads(request.body)

        tel = d["telephone"]

        t ="-".join([str(d["year"]),d["mounth"],d["day"]])
        tt = datetime.strptime(t,"%Y-%m-%d")

        content = d["addressdetails"]

        # #存储用户生日
        cursor = connection.cursor()
        sql = "UPDATE user_user set birthday = '{0}' where telephone = {1} ".format(tt,tel)
        cursor.execute(sql)

        #获取用户id
        sql = "select id from user_user WHERE telephone = {0}".format(tel)
        cursor.execute(sql)
        user_id = cursor.fetchone()[0]


        #获取与地址对应的省 市 县/区名
        sql = "select address_name from ops_address WHERE address_id = {0}".format(d["province"])
        cursor.execute(sql)
        pro = cursor.fetchone()[0]

        sql = "select address_name from ops_address WHERE address_id = {0}".format(d["city"])
        cursor.execute(sql)
        c = cursor.fetchone()[0]

        sql = "select address_name from ops_address WHERE address_id = {0}".format(d["area"])
        cursor.execute(sql)
        a = cursor.fetchone()[0]


        #存储用户的详细地址
        print(pro,c,a,user_id)
        sql = "insert into detailed_address(province_name,city_name,area,address_discribe,user_id) VALUES('{0}','{1}','{2}','{3}',{4})".format(pro,c,a,content,user_id)
        cursor.execute(sql)
        return JsonResponse({"code":"200"})


#获取发送的领养信息
def getadopt(request):
    if request.method == "POST":
        try:
            #验证token
            token = json.loads(request.body)["token"]
            c = get_token(token)

            if c == 406:
                return JsonResponse({"code": "406"})

            #分页
            pagesize = 7

            #获取信息
            id = json.loads(request.body)["id"]
            i = json.loads(request.body)["index"]
            print("id")
            cursor = connection.cursor()

            # 获取领养信息
            sql = "select a.title,state_type_id,a.stat_time,a.end_time,type.type,a.date,a.id from adopt_adopt as a ,adopt_pettype as type where a.user_id = {0} and a.pet_type_id = type.id".format(id)
            res = cursor.execute(sql)
            data = cursor.fetchall();

            d = []
            for item in data:
                j = {}
                j["name"] = item[0]
                j["stime"] = item[2]
                j["etime"] = item[3]
                j["pettype"] = item[4]
                j["newdate"] = item[5]
                j["adoptid"] = item[6]

                if item[1] == 1:
                    j["adopttype"] = "待领养"
                elif item[1] == 2:
                    j["adopttype"] = "领养中"
                elif item[1] == 3:
                    j["adopttype"] = "领养结束"
                d.append(j)
                print(item)

            dd = sorted(d,key = lambda i:i["newdate"],reverse=True)
            # dd = dd[(i-1)*pagesize:(i*pagesize)]
            dd.append({"p":res})

            print(dd)

            return JsonResponse(dd,safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"406"})


#验证token
def get_token(token):
    try:
        print(token)
        SECRET_KEY = '123456'
        # 将headers中的token进行解密
        decoded = jwt.decode(token, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
        print(decoded)

        # 判断用户名是否存在
        cursor = connection.cursor()
        sql = "select * from user_user WHERE telephone = {0}".format(decoded["user_id"]["telephone"])
        res = cursor.execute(sql)

        if res == 1:
            return "验证通过"
        else:
            return 406  #没有找到用户

    except Exception as ex:
        print(ex)
        return 406

#获取个人中心导航栏中的头像和名称
def getnameimg(request):
    if request.method == 'POST':
        id = json.loads(request.body)["id"]
        cursor = connection.cursor()

        # 获取用户的基本信息
        sql = "select u.name,u.photo from user_user as u where id = {0}".format(id)
        res = cursor.execute(sql)
        data = cursor.fetchone();
        d = {
            "name":data[0],
            "touxiang":data[1]
        }

        return JsonResponse(d)


def getpets(request):
    if request.method == 'POST':
        try:
            print(request)
            userid = json.loads(request.body)["id"]
            cursor = connection.cursor()

            sql = "select li.name,li.state,a.title,a.stat_time,a.end_time,ad.type from lingyang_lingyang as li, adopt_adopt as a,adopt_pettype as ad WHERE lingyang_user_id_id = {0} and li.adopt_uer_id_id = a.id and a.pet_type_id = ad.id".format(userid)
            res = cursor.execute(sql);
            row = cursor.fetchall();
            data = []
            for item in row:
                print(item)
                j = {}

                j["name"] = item[0]

                j["contact"] = item[2]

                j["type"] = item[-1]

                j["stat_time"] = item[3]

                j["end_time"] = item[4]
                j["state"] = item[1]

                data.append(j)

            n = len(data)
            data.append({"n":n})
            print(n)


        # return HttpResponse(json.dumps(data[pagesize * (index - 1):pagesize * index], ensure_ascii=False))
            return JsonResponse(data,safe = False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "409"})

