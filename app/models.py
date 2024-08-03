from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Certificates(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  score = models.CharField(max_length=10)

 