# coding:utf-8

from django.db import models


class SaveCpu(models.Model):
    used = models.FloatField()
    time = models.DateTimeField()

# Create your models here.
