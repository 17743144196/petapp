from django.db import models
from user.models import *

# Create your models here.
class show(models.Model):
    user=models.ForeignKey(to=user,to_field="id",on_delete=models.CASCADE)
    contents = models.CharField(max_length=300, null=True)
    photo = models.CharField(max_length=100,null=True)
    liulan = models.IntegerField(default=0)
    zan = models.IntegerField(default=0)
    pinglun = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

class showcomment(models.Model):
    show=models.ForeignKey(to="show",to_field="id",on_delete=models.CASCADE)
    content=models.CharField(max_length=300,null=True)
    user = models.ForeignKey(to=user, to_field="id", on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)


