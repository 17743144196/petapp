from django.conf.urls import url

from . import views
app_name = 'user'
#user子路由
urlpatterns = [
    # url(r'^$',views.personal,name='personal'),
    # 后面的/不能省略
    url(r'login/', views.login, name='login'),
    # url(r'add/', views.add, name='add'),
    # url(r'query/', views.query, name='query'),
    url(r'regist/', views.register, name='register'),
    url(r'sendcode/', views.sendcode, name='sendcode'),
    url(r'yezheng/', views.yezheng, name='yezheng'),
    url(r'getNameImg/', views.getNameImg, name='getNameImg'),
    # url(r'^getuser\w*/(?P<id>\d*)', views.getuserbyid, name='getuser'),
    # url(r'changepassword/', views.changepassword, name='changepassword'),
    url(r'yanzhengemail/', views.yanzhengemail, name='yanzhengemail'),
    url(r'addemail/', views.addemail, name='addemail'),
    url(r'chackphone/', views.chackphone, name='chackphone'),
    url(r'sendEmail/', views.sendEmail, name='sendEmail'),
    url(r'realname/',views.realname,name = "realname"), #用于实名认证
    url(r'repassword/',views.repassword,name = "repassword"), #用于实名认证

]
