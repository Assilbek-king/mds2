from django.db import models
from main.models import *
# Create your views here.


class Slider(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return f'{self.title}'

class Example(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)


    def __str__(self):
        return f'{self.logo}'

class Partner(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)


    def __str__(self):
        return f'{self.logo}'

class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    message = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.name} {self.phone}'


class Category(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=1,blank=True) #1 vhodnoy 2 kvartira 3 furnitura

    def __str__(self):
        return f'{self.title}'

class Tovar(models.Model):
    logo1 = models.ImageField(upload_to='upload', blank=True)
    logo2= models.ImageField(upload_to='upload', blank=True)
    logo3 = models.ImageField(upload_to='upload', blank=True)
    logo4 = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    pokritiya_metalla = models.TextField(max_length=500, blank=True)
    narujniy_panel = models.TextField(max_length=500, blank=True)
    vnutnennit_panel = models.TextField(max_length=500, blank=True)
    osnovnoy_zamok = models.TextField(max_length=500, blank=True)
    dop_zamok = models.TextField(max_length=500, blank=True)
    furnitura = models.TextField(max_length=500, blank=True)
    dop_info = models.TextField(max_length=500, blank=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.title} {self.cat.title}'