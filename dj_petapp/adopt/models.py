from django.db import models
from user.models import *
# # # Create your models here.
# # # 创建寄养订单表
class adopt(models.Model):

# 用户外键
    user=models.ForeignKey(to=user,to_field="id",on_delete=models.CASCADE)
# 类型
    pet_type= models.ForeignKey(to="pettype",to_field="id",on_delete=models.CASCADE)
# 性别
    pet_sex =models.ForeignKey(to="petsex",to_field="id",on_delete=models.CASCADE)
# 标题
    title= models.CharField(max_length=100)
# pet照片
    picone= models.CharField(max_length=100,null=True)
    pictwo= models.CharField(max_length=100,null=True)

# 介绍
    introduce = models.CharField(max_length=300)
# 开始时间结束时间
    stat_time=models.CharField(max_length=50,null=True)
    end_time=models.CharField(max_length=50,null=True)
# 要求
    yaoqiu = models.CharField(max_length=300)
#是否免费
    isFree = models.CharField(max_length=50)
    # 价格
    price = models.IntegerField(null=True)
# 围观
    onlooker = models.CharField(max_length=50,default=0)
# 喜欢
    like=models.CharField(max_length=50,default=0)
# 评论数
    com_num=models.CharField(max_length=50,default=0)
#     分享数
    share=models.CharField(max_length=50,default=0)
    # 发布时间
    date = models.DateTimeField(auto_now_add=True)
#
    citys = models.CharField(max_length=50,null=True)
    areas = models.CharField(max_length=50,null=True)
    provid=models.ForeignKey(to="province",to_field="pycode",on_delete=models.CASCADE)
    # cityid=models.ForeignKey(to="city",to_field="id",on_delete=models.CASCADE)
    # areaid=models.ForeignKey(to="area",to_field="id",on_delete=models.CASCADE)
    # 联系人信息
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    weixin = models.CharField(max_length=50,null=True)
    qq = models.CharField(max_length=50,null=True)
# 状态外键
    state_type=models.ForeignKey(to="state",to_field="id",on_delete=models.CASCADE,default=1)

# # # 创建订单状态表
class state(models.Model):
    type=models.CharField(max_length=10,unique=True)

# 创建宠物类型表
class pettype(models.Model):
    type=models.CharField(max_length=15,unique=True)

# 宠物性别表
class petsex(models.Model):
    sex=models.CharField(max_length=15,unique=True)
 # 省份表
class province(models.Model):
    name=models.CharField(max_length=50)
    pycode=models.IntegerField(unique=True)
# adopt的评论表
class comment(models.Model):
    pet=models.ForeignKey(to="adopt",to_field="id",on_delete=models.CASCADE)
    content=models.CharField(max_length=300,null=True)
    user = models.ForeignKey(to=user, to_field="id", on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
# 点赞表
class zan(models.Model):
    user = models.ForeignKey(to=user, to_field="id", on_delete=models.CASCADE)
    pet = models.ForeignKey(to="adopt", to_field="id", on_delete=models.CASCADE)
