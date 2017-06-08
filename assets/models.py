# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Port(models.Model):
    ip = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    createtime = models.DateTimeField()
    class Meta:
        db_table = 'portscan_main'


class Iplist(models.Model):
    ip = models.CharField(max_length=255)
    port = models.TextField()
    createtime = models.DateTimeField()
    class Meta:
        db_table = 'iplist'

class Domain(models.Model):
    domain = models.CharField(max_length=255)
    statue = models.IntegerField(default=0)
    createtime = models.DateTimeField()
    class Meta:
        db_table = 'domain'
