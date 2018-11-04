from django.db import models
from adopt.models import *
from user.models import *

# Create your models here.
class lingyang (models.Model):
    lingyang_user_id=models.ForeignKey(to=user,to_field="id",on_delete=models.CASCADE)
    adopt_uer_id=models.ForeignKey(to=adopt,to_field="id",on_delete=models.CASCADE)
    reason = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=20,default="领养中")
    telepthone = models.CharField(max_length=11,null=True)
    name = models.CharField(max_length=20,null=True)
    display=models.CharField(max_length=20,default=1)


