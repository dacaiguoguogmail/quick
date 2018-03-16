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
    usermodel = models.ForeignKey(UserModel2, on_delete=models.CASCADE)
    av = models.CharField(max_length=200, blank=True)
    an = models.CharField(max_length=200, blank=True)
    ec = models.CharField(max_length=200, blank=True)
    rsd = models.CharField(max_length=200, blank=True)
    scsd = models.CharField(max_length=200, blank=True)
    ecd = models.CharField(max_length=200, blank=True)
    nt = models.CharField(max_length=200, blank=True)
    rft = models.CharField(max_length=200, blank=True)
    i10 = models.CharField(max_length=200, blank=True)
    sced = models.CharField(max_length=200, blank=True)
    iuf = models.CharField(max_length=200, blank=True)
    red = models.CharField(max_length=200, blank=True)
    fsd = models.CharField(max_length=200, blank=True)
    spsd = models.CharField(max_length=200, blank=True)
    dlsd = models.CharField(max_length=200, blank=True)
    sped = models.CharField(max_length=200, blank=True)
    dz = models.CharField(max_length=200, blank=True)
    pi = models.CharField(max_length=200, blank=True)
    rt = models.CharField(max_length=200, blank=True)
    rc = models.CharField(max_length=200, blank=True)
    dled = models.CharField(max_length=200, blank=True)
    csd = models.CharField(max_length=200, blank=True)
    re = models.CharField(max_length=200, blank=True)
    at = models.CharField(max_length=200, blank=True)
    npn = models.CharField(max_length=200, blank=True)
    pc = models.CharField(max_length=200, blank=True)
    ced = models.CharField(max_length=200, blank=True)
    cp = models.CharField(max_length=200, blank=True)