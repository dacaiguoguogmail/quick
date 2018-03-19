from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=True)
    votes = models.IntegerField(default=0)


class UserModel2(models.Model):
    def __str__(self):
        return self.dt
    lo = models.CharField(max_length=200, blank=True)
    la = models.CharField(max_length=200, blank=True)
    prov = models.CharField(max_length=200, blank=True)
    dt = models.CharField(max_length=200, blank=True)
    tec = models.CharField(max_length=200, blank=True)
    ct = models.CharField(max_length=200, blank=True)
    ui = models.CharField(max_length=200, blank=True)
    ns = models.CharField(max_length=200, blank=True)
    ver = models.CharField(max_length=200, blank=True)
    ot = models.CharField(max_length=200, blank=True)
    mn = models.CharField(max_length=200, blank=True)


class UserDataModel2(models.Model):
    def __str__(self):
        return self.av    
    i10 = models.BooleanField(default=False)#is >= iOS 10
    ecd = models.IntegerField(default=0) #error code
    fsd = models.FloatField(default=0)#fetchStartDate
    dlsd = models.FloatField(default=0)#domainLookupStartDate
    dled = models.FloatField(default=0)#domainLookupEndDate
    csd = models.FloatField(default=0)#connectStartDate
    scsd = models.FloatField(default=0)#secureConnectionStartDate
    sced = models.FloatField(default=0)#secureConnectionEndDate
    ced = models.FloatField(default=0)#connectEndDate
    rsd = models.FloatField(default=0)#requestStartDate
    red = models.FloatField(default=0)#requestEndDate
    rpsd = models.FloatField(default=0)#responseStartDate
    rped = models.FloatField(default=0)#responseEndDate
    npn = models.CharField(max_length=19, default="")#networkProtocolName
    pc = models.BooleanField(default=False)#proxyConnection
    rc = models.BooleanField(default=False)#reusedConnection
    rft = models.CharField(max_length=19, default="")#resourceFetchType

    an = models.CharField(max_length=200, blank=True)#(api name)接口名
    dz = models.CharField(max_length=200, blank=True)#(data size)数据包大小
    av = models.CharField(max_length=200, blank=True)#(api version)接口版本号 版本号为空传NONE
    rt = models.CharField(max_length=200, blank=True)#(request type)请求类型 1:POST 2:GET 3:PATCH 4:PUT 5:DELETE 6:其他
    ec = models.CharField(max_length=200, blank=True)#（error code）接口请求失败对应的异常code放入这边，包括接口异常和HTTP请求异常,如果ec为1则表示请求成功
    cp = models.CharField(max_length=200, blank=True)#(Custom Parameter) 自定义参数 （接口请求失败对应的异常code放入这边）
    pi = models.CharField(max_length=200, blank=True)#(page id) 页面编号（该接口属于哪个页面）
    usermodel = models.ForeignKey(UserModel2, on_delete=models.CASCADE)

    