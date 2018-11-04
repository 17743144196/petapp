from django.conf.urls import url

from . import views
app_name = 'adopt'
#user子路由
urlpatterns = [
    url(r'^search\w*/', views.search, name='search'),
    url(r'^DicLoad/', views.DicLoad, name='DicLoad'),
    url(r'^FlieName/', views.FlieName, name='FlieName'),
    url(r'^pettype\w*/', views.pettype, name='pettype'),
    url(r'^randadopt\w*/', views.randadopt, name='randadopt'),
    # url(r'^add\w*/', views.add, name='add'),
    url(r'^showcomment\w*/(?P<a>\d*)/', views.showcomment, name='showcomment'),
    url(r'^comment\w*/', views.comment, name='comment'),
    url(r'^adoptpp\w*/(?P<index>\d*)/(?P<con>\w*)/', views.adoptpp, name='adoptpp'),
    url(r'^acount\w*/(?P<con>.*)/', views.acount, name='acount'),

    # url(r'^adoptpp\w*/', views.adoptpp, name='adoptpp'),
    url(r'^getpets\w*/(?P<index>\d*)/(?P<con>\w*)/(?P<tp>\w*)/', views.getpets, name='getpets'),
    url(r'^adopts\w*/(?P<iid>\w*)/', views.adopts, name='adopts'),
    url(r'^dianzan\w*/', views.dianzan, name='dianzan'),
    # url(r'^getadopts\w*/(?P<index>\d*)/(?P<con>\w*)/', views.getadopts, name='getadopts')
]
