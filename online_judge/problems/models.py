from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=30,unique=True)
    content = models.TextField()
    difficulty = models.CharField(max_length=20)
    inputTestCasePath = models.CharField(max_length=200)
    outputTestCasePath = models.CharField(max_length=200)
    

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    verdict = models.CharField(max_length=30);
    submitted_time = models.DateTimeField(default=timezone.now)
    submitted_code = models.TextField()


