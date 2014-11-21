from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Vimage(models.Model):  
    id = models.AutoField(primary_key=True)  
    img_url = models.CharField(max_length=1000)  
    def __unicode__(self):  
        return self.img_url


class Pmachine(models.Model):  
    id = models.AutoField(primary_key=True)  
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    cpu = models.CharField(max_length=20)
    disk = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    maxvm = models.IntegerField()
    def __unicode__(self):  
        return self.ip

class Vmachine(models.Model):  
    id = models.AutoField(primary_key=True)  
    ip = models.GenericIPAddressField(unpack_ipv4=True)
    netmask = models.CharField(max_length=20)  
    gateway = models.CharField(max_length=20)
    pmachine = models.ForeignKey(Pmachine,related_name = "vmachines")
    vimage   = models.ForeignKey(Vimage,related_name = "vmachines")
    states = models.CharField(max_length=20)
    def __unicode__(self):  
        return self.ip

class Task(models.Model):  
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey(User)
    vimage = models.ForeignKey(Vimage)
    vmachine = models.OneToOneField(Vmachine)
    createdtime = models.DateTimeField()
    uuid = models.CharField(max_length=40,null=True)  
    def __unicode__(self):  
        return str(self.id)
