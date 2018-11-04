from django.conf.urls import url

from . import views
app_name = 'forum'
#user子路由
urlpatterns = [
    url(r'^forumtype\w*/', views.forumtype, name='forumtype'),
    url(r'^getforum\w*/(?P<index>\d*)/(?P<tp>\w*)/', views.getforum, name='getforum'),
    url(r'^search\w*/(?P<a>\d*)/', views.search, name='search'),
    url(r'^comment\w*/', views.comment, name='comment'),
    url(r'^forumcomment\w*/(?P<a>\d*)/', views.forumcomment, name='forumcomment'),
]
