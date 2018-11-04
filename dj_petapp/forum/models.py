from django.db import models
from user.models import *
# Create your models here.
# 创建论坛表
class forum(models.Model):
    user=models.ForeignKey(to=user,to_field="id",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    picture=models.CharField(max_length=200)
    content=models.CharField(max_length=4000)
    zan = models.IntegerField(default=0)
    lookers = models.IntegerField(default=0)
    type=models.ForeignKey(to="type",to_field="id",on_delete=models.CASCADE)
    # 联系人：小石头
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    weixin = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)

#
# class comment(models.Model):
#     forum = models.ForeignKey(to="forum", to_field="id", on_delete=models.CASCADE)
#     comment_user=models.ForeignKey(to=userbasic, to_field="name", on_delete=models.CASCADE)
#     content=models.CharField(max_length=400)
#     praise=models.IntegerField(null=True)
#
# 论坛文章类型表
class type(models.Model):
    type = models.CharField(max_length=50)
# 评论表
class forumcomment(models.Model):
    forum = models.ForeignKey(to="forum", to_field="id", on_delete=models.CASCADE)
    content=models.CharField(max_length=300,null=True)
    user = models.ForeignKey(to=user, to_field="id", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
