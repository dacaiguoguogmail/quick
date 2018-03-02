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
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class UserModel2(models.Model):
    def __str__(self):
        return self.dt
    lo = models.CharField(max_length=200)
    prov = models.CharField(max_length=200)
    dt = models.CharField(max_length=200)
    tec = models.CharField(max_length=200)
    ct = models.CharField(max_length=200)
    ui = models.CharField(max_length=200)
    ns = models.CharField(max_length=200)
    ver = models.CharField(max_length=200)
    ot = models.CharField(max_length=200)
    mn = models.CharField(max_length=200)


class UserDataModel2(models.Model):
    def __str__(self):
        return self.av
    
    usermodel = models.ForeignKey(UserModel2, on_delete=models.CASCADE)
    av = models.CharField(max_length=200)
    an = models.CharField(max_length=200)
    ec = models.CharField(max_length=200)
    rsd = models.CharField(max_length=200)
    scsd = models.CharField(max_length=200)
    ecd = models.CharField(max_length=200)
    nt = models.CharField(max_length=200)
    rft = models.CharField(max_length=200)
    i10 = models.CharField(max_length=200)
    sced = models.CharField(max_length=200)
    iuf = models.CharField(max_length=200)
    red = models.CharField(max_length=200)
    fsd = models.CharField(max_length=200)
    spsd = models.CharField(max_length=200)
    dlsd = models.CharField(max_length=200)
    sped = models.CharField(max_length=200)
    dz = models.CharField(max_length=200)
    pi = models.CharField(max_length=200)
    rt = models.CharField(max_length=200)
    rc = models.CharField(max_length=200)
    dled = models.CharField(max_length=200)
    csd = models.CharField(max_length=200)
    re = models.CharField(max_length=200)
    at = models.CharField(max_length=200)
    npn = models.CharField(max_length=200)
    pc = models.CharField(max_length=200)
    ced = models.CharField(max_length=200)
    cp = models.CharField(max_length=200)