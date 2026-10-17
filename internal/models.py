from django.db import models
import time

# Create your models here.
class Banner(models.Model):
    bannerid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=100, null=False)
    enable = models.BooleanField(default=True)
    addtime = models.BigIntegerField(editable=False)
    
    def save(self, *args, **kwargs):
        now = int(time.time())
        # self.lastUpdate = now     
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
       
        
class Info(models.Model):
    infoid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    imgpath = models.CharField(max_length=100, null=False)
    enable = models.BooleanField(default=True)
    addtime = models.BigIntegerField(editable=False) 
    
    def save(self, *args, **kwargs):
        now = int(time.time())
        # self.lastUpdate = now     
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)


class History(models.Model):
    historyid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False)
    addtime = models.BigIntegerField(editable=False)
    lastUpdate = models.BigIntegerField(editable=False)

    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)


class FeatureType(models.Model):    
    featuretypeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    chinese_name = models.TextField(null=False)
    enable = models.BooleanField(default=True)
        
    
class FeatureInfo(models.Model):    
    featureinfoid = models.AutoField(primary_key=True)
    topic = models.ForeignKey('FeatureType', on_delete=models.CASCADE)
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    addtime = models.BigIntegerField(editable=False)
    lastUpdate = models.BigIntegerField(editable=False)

    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)

        
class Category(models.Model):    
    categoryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    enable = models.BooleanField(default=True)

class Item(models.Model):    
    itemid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    imgpath = models.CharField(max_length=100)
    dimension = models.TextField(null=False)
    material = models.CharField(max_length=100, null=False)
    info = models.TextField(null=False)
    categoryid = models.ForeignKey('Category', on_delete=models.CASCADE)
    addtime = models.BigIntegerField(editable=False)
    lastUpdate = models.BigIntegerField(editable=False)
    
    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
        

class News(models.Model):    
    newsid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False)
    addtime = models.BigIntegerField()
    lastUpdate = models.BigIntegerField()

    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
        

class Faq(models.Model):    
    faqid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, null=False)
    answer = models.TextField(null=False)
    addtime = models.BigIntegerField(editable=False)
    lastUpdate = models.BigIntegerField(editable=False)

    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
        
        
class Downloads(models.Model):    
    downloadsid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    filepath = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=30, null=False)
    version = models.CharField(max_length=30, null=False)
    info = models.TextField(null=False)
    addtime = models.BigIntegerField(editable=False)
    lastUpdate = models.BigIntegerField(editable=False)

    def save(self, *args, **kwargs):
        now = int(time.time())
        self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
        

class Company(models.Model):    
    name = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    fax = models.CharField(max_length=20)  
    servicetime = models.TextField(null=False)

class Form(models.Model):    
    formid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=30)
    contactname = models.CharField(max_length=10)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False)
    addtime = models.BigIntegerField()

    def save(self, *args, **kwargs):
        now = int(time.time())
        # self.lastUpdate = now
        
        if not self.pk:
            self.addtime = now
            
        super().save(*args, **kwargs)
        

class Message(models.Model):    
    messageid = models.AutoField(primary_key=True)
    formid = models.ForeignKey('Form', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)
    lastUpdate = models.BigIntegerField()
    
    def save(self, *args, **kwargs):
       now = int(time.time())
       self.lastUpdate = now
       
       # if not self.pk:
       #     self.addtime = now
           
       super().save(*args, **kwargs)