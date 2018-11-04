from django.conf.urls import url
from . import views
import uuid
app_name = "personal"
urlpatterns = [
    # url(r'^acountjobs\w*/(?P<con>.*)/', views.acount, name='acount'),
    #     # url(r'^add\w*/', views.add, name='add'),
    #     # url(r'^getjobs\w*/(?P<index>\d*)/(?P<con>\w*)/', views.getjobs, name='getjobs'),
    # url(r'^personal/',views.personal,name = "personals")
    url(r'^$',views.personal, name = "index"),
    url(r'^safety/',views.safety, name = "safety"),
    url(r'upload/', views.upload, name='upload'),  # 用户上传头像准备工作，签发七牛云token，处理文件名
    url(r'qiniu/',views.qiniu,name = "qiniutoken"),
    url(r'uploadimg/',views.uploadimg,name = "uploadimg"),
    url(r'getInformation/',views.getInformation,name = "getInformation"),
    url(r'sendcode/',views.sendcode,name = "sendcode"), #发送短信
    url(r'alterp/',views.alterp,name = "alterp"), #修改密码
    url(r'getProvince/',views.getProvince,name = "getProvince"), #获取省地址
    url(r'getCity/',views.getCity,name = "getCity"), #获取市地址
    url(r'getAare/',views.getAare,name = "getAare"), #获取区地址
    url(r'savasd/',views.savasd,name = "savasd"), #用于存储控制中心上传的地址和日期
    url(r'getadopt/',views.getadopt,name = "getadopt"), #用户获取寄养记录
    url(r'getnameimg/',views.getnameimg,name = "getnameimg"),
    url(r'^getpets/', views.getpets, name='getpets'),  # 用户获取领养记录
]