# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from blueking.component.shortcuts import get_client_by_request
from home_application.celery_tasks import async_task, execute_task, get_time
from home_application.models import HostInfo
from datetime import datetime


def home(request):
    """
    首页
    """
    # 调用自己开发的API组件
    client = get_client_by_request(request)
    kwargs = {'token': '@adf*adsd^'}
    resp = client.cm.get_capacity(**kwargs)

    # 执行celery异步任务
    # async_task.delay(1, 2, 1)

    # 执行定时任务
    # execute_task(2)
    return render_mako_context(request, '/home_application/home.html', {'result': resp})
def hostinfo_mwptest3(request):
    """
        主机信息新增和查询
    """
    if request.method == 'POST':
        host=request.POST.get('host',None)
        ip=request.POST.get('ip',None)
        systemtype=request.POST.get('systemtype',None)
        diskdir=request.POST.get('diskdir',None)
        if host and ip and systemtype and diskdir:
            try:
                HostInfo.objects.create(host=host,ip=ip,systemtype=systemtype,diskdir=diskdir,createtime=datetime.now())
            except Exception as e:
                return render_json({'code':'-1','message':str(e)})
            return render_json({'code':'0','message':"insert success"})
    allHost=HostInfo.objects.all().order_by('-id')
    data = []
    for index, info in enumerate(allHost):
        data.append({
            'index': index,
            'host': info.host,
            'ip': info.ip,
            'systemtype': info.systemtype,
            'diskdir': info.diskdir,
            'createtime': info.createtime.strftime('%Y-%m-%d %H:%M:%S')
        })
#    return render_json({'data':data})
    return render_json({"catalogues":{
        "index":"#",
        "host":"主机名",
        "ip":"位置",
        "systemtype":"操作系统类型",
        "diskdir":"磁盘目录",
        "createtime":"创建时间"
    },"items":data})

def mwptest3(request):
    return render_mako_context(request, '/home_application/mwptest3.html')

def mwptest1(request):
    """
        输入参数并返回
    """
    if request.POST:
        input1=str(request.POST.get('input1',None))
        if input1 == 'Hello&nbsp;Blueking' or input1 == 'Hello Blueking':
        #result="Congratulation！"
            return render_json({'result':'Congratulation！'})
        # else:
        #     return render_json({'result':input1})
    return render_mako_context(request, '/home_application/mwptest.html')

def test(request):
    """
    开发指引
    """
    data = {
        'data1': 11,
        'data2': 22,
    }
    return render_mako_context(request, '/home_application/test.html', {'data': data})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def helloworld(request):
    """
    helloworld
    """
    return render_mako_context(request, '/home_application/helloworld.html')
