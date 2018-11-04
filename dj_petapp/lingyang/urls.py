from django.conf.urls import url

from . import views
app_name = 'lingyang'
#user子路由
urlpatterns = [
    url(r'^xinxi\w*/', views.xinxi, name='xinxi'),
    url(r'^checkemail\w*/', views.checkemail, name='checkemail'),
    url(r'^showlingyang\w*/', views.showlingyang, name='showlingyang'),
    url(r'^dellingyang/', views.dellingyang, name='dellingyang'),
    url(r'^confirm\w*/', views.confirm, name='confirm'),
    url(r'^cancel\w*/', views.cancel, name='cancel')

]
