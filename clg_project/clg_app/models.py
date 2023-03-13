from django.db import models


class Clg(models.Model):
    name = models.CharField(max_length=180)
    img = models.ImageField(upload_to='pics',max_length=300*188)
    desc = models.TextField()


class Register(models.Model):
    name = models.CharField(max_length=180)
    password=models.CharField(max_length=50)



def __str__(self):
    return self.name
