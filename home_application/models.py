# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from common.log import logger


class HostDataManager(models.Manager):
    def save_data(self, data):
        """
        保存执行结果数据
        """
        try:
            HostInfo.objects.create(
                host=data[0],
                ip=data[1],
                systemtype=data[2],
                diskdir=data[3],
                createtime=datetime.now()
            )
            result = {'result': True, 'message': u"保存成功"}
        except Exception, e:
            logger.error(u"save_data %s" % e)
            result = {'result': False, 'message': u"保存失败, %s" % e}
        return result


class HostInfo(models.Model):
    """
    存储查询的容量数据
    """
    host = models.CharField('host', max_length=128, blank=True, null=True)
    ip = models.CharField('ip', max_length=64, blank=True, null=True)
    systemtype = models.CharField('systemtype', max_length=64, blank=True, null=True)
    diskdir = models.CharField('diskdir', max_length=64)
    createtime =  models.DateTimeField(u"保存时间")
    objects = HostDataManager()

    
    def __unicode__(self):
        return self.systemtype

    class Meta:
        verbose_name = u"主机名"
        verbose_name_plural = u"主机IP"
