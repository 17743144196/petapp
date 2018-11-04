from django.conf.urls import url

from . import views
app_name = 'petshow'
#user子路由
urlpatterns = [
    url(r'^DicLoad/', views.DicLoad, name='DicLoad'),
    url(r'^FlieName/', views.FlieName, name='FlieName'),
    url(r'^showp\w*/(?P<index>\d*)/', views.showp, name='showp'),
    url(r'^showdetail\w*/(?P<a>\d*)/', views.showdetail, name='showdetail'),
    url(r'^comments\w*/', views.comments, name='comments'),
    url(r'^showcomments\w*/(?P<a>\d*)/', views.showcomments, name='showcomments'),
    url(r'^acountpets\w*/(?P<con>.*)/', views.acount, name='acount'),
    # url(r'^searchphoto\w*/(?P<b>\d*)/', views.searchphoto, name='searchphoto'),


]
