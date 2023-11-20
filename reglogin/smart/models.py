from django.db import models

class product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=50)
    pcost=models.BigIntegerField()
    pmfdt=models.DateField()
    pexpdt=models.DateField()
