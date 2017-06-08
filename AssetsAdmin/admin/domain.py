# -*- coding: utf-8 -*-

from assets.models import Domain

from django.http import HttpResponse
from django.shortcuts import render
from datetime import  datetime


def index(request):
    list = Domain.objects.all()
    return render(request,'admin/domain.html',{'domainlist':list})



def add(request):
    if request.method == 'GET':
        return render(request,'admin/domain/add.html')
    if request.method == 'POST':
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        domains= request.POST.get('domain')
        obj = Domain(domain=domains,createtime=now)
        obj.save()
        return HttpResponse("<p>数据添加成功！</p>")