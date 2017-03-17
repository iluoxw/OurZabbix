# coding: utf-8
import datetime
from django.http import JsonResponse
from django.shortcuts import render_to_response
from models import *


def saveCpu(request):
    """
    当被请求时，会将请求上来的数据存入数据库
    :param request:
    :return:
    """
    status = {}
    if request.method == "POST" and request.POST:
        # 检测请求的方式是POST，并且post请求有数据
        # request.POST这个方法以字典的方式存放着当前post请求的所有数据
        cpu_used = request.POST["cpu_used"]
        # 使用类字典的取值方式取出传递上来的cpu使用率
        time = datetime.datetime.now()
        # 获取当前时间
        cpu_Database = SaveCpu()
        # 实例化一个SaveCpu的模型实例
        cpu_Database.used = cpu_used
        # 将数据赋值给模型
        cpu_Database.time = time
        # 将时间赋值给模型
        cpu_Database.save()
        # 将模型映射到数据库
        status["status"] = "success"
        # 定义当前接口状态为保存成功
    else:
        status["status"] = "request method must be post"
        # 定义当前接口状态为失败

    return JsonResponse(status)
    # 将接口状态返回给请求者

# Create your views here.
