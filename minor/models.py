from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Logg(models.Model):
    name=models.CharField(max_length=50, default='')
    department=models.CharField(max_length=40,default='')
    authid=models.CharField(max_length=50,default='')
    question=models.CharField(max_length=200,default='')
    answer = models.CharField(max_length=200, default='')
    confirm=models.CharField(max_length=5,default=False,help_text="yes/no")
    upvote=models.IntegerField(default=0)




