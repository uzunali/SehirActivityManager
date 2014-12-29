# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class AddActivity(models.Model):
    Activity_Name = models.CharField(max_length=200,blank=True,unique=True)
    Speaker=models.CharField(max_length=200,blank=True)
    Time=models.DateField(blank=True)
    Place=models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='uploadeds', blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.Activity_Name



class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "Time", "Activity_Name", "Speaker"]
    list_filter = ["creator"]
    info=["explanention"]


