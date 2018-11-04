from django.db import models

# Create your models here.
# 用户表
class user(models.Model):
    telephone=models.CharField(max_length=11,unique=True)
    password=models.CharField(max_length=200)
    creat_datetime=models.DateTimeField(auto_now_add=True)
    photo = models.CharField(max_length=300, default='https://wx.qlogo.cn/mmopen/vi_32/jQNyKqaK3ibLEm7L5z6UFBrJ5nVlvzZ9am4PjH2X93uj0ucTOGNcTSBsPbgmUgVicwgqomzaibYWIib0F5jlTgLmmw/132')
    name = models.CharField(max_length=50)
    login_time=models.CharField(max_length=50,null=True)
    last_time=models.CharField(max_length=50,null=True)
    login_num=models.CharField(max_length=50,null=True)
    email =models.CharField(max_length=50,null=True)

class userbasic(models.Model):
    user=models.ForeignKey(to=user,to_field='id',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    idcard=models.CharField(max_length=20, unique=True)
    leixing=models.CharField(max_length=20, unique=True)
    bankcard=models.CharField(max_length=20, unique=True)
    telephone = models.CharField(max_length=11, unique=True)
    # password = models.CharField(max_length=200)
    # creat_datetime = models.DateTimeField(auto_now_add=True)
    # photo = models.CharField(max_length=300,
    #                          default='https://wx.qlogo.cn/mmopen/vi_32/jQNyKqaK3ibLEm7L5z6UFBrJ5nVlvzZ9am4PjH2X93uj0ucTOGNcTSBsPbgmUgVicwgqomzaibYWIib0F5jlTgLmmw/132')

    # login_time = models.CharField(max_length=50, null=True)
    # last_time = models.CharField(max_length=50, null=True)
    # login_num = models.CharField(max_length=50, null=True)
    # email = models.CharField(max_length=50, null=True)


#
#     # xx=models.AutoField   自增
# # class userbase(models.Model):
# #     xxx=models.ForeignKey(to=user,to_field='telephone',on_delete=models.CASCADE)
# # 省份表
# class province(models.Model):
#     name=models.CharField(max_length=50)
#     pycode=models.IntegerField(unique=True)
#
# # 城市表
# class city (models.Model):
#     name = models.CharField(max_length=50)
#
#     province_id = models.ForeignKey(to="province",to_field='pycode',on_delete=models.CASCADE)
#
# # 用户基本信息表
# class userbasic(models.Model):

#
#     telephone=models.ForeignKey(to="user",to_field="telephone",on_delete=models.CASCADE)
#     id_card=models.CharField(max_length=50)

#     uer_id=models.IntegerField(unique=True)
#
# # 用户地址表
# class useraddress(models.Model):
#     province_pycode=models.ForeignKey(to="province",to_field="pycode",on_delete=models.CASCADE)
#     city_id=models.ForeignKey(to="city",to_field="id",on_delete=models.CASCADE)
#     address=models.CharField(max_length=200)
#     user_id=models.ForeignKey(to="userbasic",to_field="uer_id",on_delete=models.CASCADE)
#
#
# # 创建宠物类型表
# class pettype(models.Model):
#     type=models.CharField(max_length=15,unique=True)
# # 宠物性别表
# class petsex(models.Model):
#     sex=models.CharField(max_length=15,unique=True)
# # 创建宠物详情表
# class petbasic(models.Model):
#     user_id=models.ForeignKey(to="userbasic",to_field="uer_id",on_delete=models.CASCADE)
#     pet_type=models.ForeignKey(to="pettype",to_field="type",on_delete=models.CASCADE)
#     pet_photo=models.CharField(max_length=200,null=True)
#     pet_name=models.CharField(max_length=20,)
#     pet_birthday=models.DateTimeField(null=True)
#     pet_sex=models.ForeignKey(to="petsex",to_field="id",on_delete=models.CASCADE)
#     pet_weight=models.IntegerField()
#     sterilisation=models.IntegerField()   # 是否绝育
#     naughty=models.IntegerField()# 是否顽皮
#     timid=models.IntegerField()# 是否胆小
# # 创建区表
# class area (models.Model):
#     name = models.CharField(max_length=50)
#     city_id=models.ForeignKey(to="city",to_field="id",on_delete=models.CASCADE)