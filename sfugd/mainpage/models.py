#-*- coding: utf-8 -*-
# Create your models here.
from django.db import models

class Menu_one(models.Model):
        item_one = models.CharField(max_length=10, null=True)
        item_en = models.CharField(max_length=10, null=True)
        html_one = models.CharField(max_length=20, null=True)
        fafa_one = models.CharField(max_length=20, null=True)
        def __str__(self):
                return self.item_one
        
class Content_2(models.Model):
        text_2 = models.TextField(null=True)
        text_en = models.TextField(null=True)
        comment_ru = models.TextField(null=True)
        comment_en = models.TextField(null=True)
        
class Info_sec(models.Model):
        brief_part = models.CharField(max_length=20, null=True)
        brief_en = models.CharField(max_length=20, null=True)
        info_part = models.TextField(null=True)
        info_en = models.TextField(null=True)
        url_part = models.CharField(max_length=50, null=True)
        def __str__(self):
                return self.brief_part  
        
class Idea_sec(models.Model):
        offer_part = models.CharField(max_length=20, null=True)
        offer_en = models.CharField(max_length=20, null=True)
        text_part = models.TextField(null=True)
        text_en = models.TextField(null=True)
        link_part = models.CharField(max_length=50, null=True)
        linkname_part = models.CharField(max_length=20, null=True)
        linkname_en = models.CharField(max_length=20, null=True)
        def __str__(self):
                return self.offer_part

