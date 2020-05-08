import pytz
from django.db import models
from timezone_field import TimeZoneField
from django.conf import settings
from django.utils import timezone


class Member(models.Model):
    id = models.AutoField(primary_key=True )
    real_name = models.CharField(max_length=40, null=True, blank=True)
    tz = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.real_name


class Period(models.Model):
    member = models.ForeignKey(Member,related_name = 'period_def',  on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(blank=True, null=True)

    def _str_(self):
        return self.start
class Main_class(models.Model):
    ok = models.BooleanField()
    members = models.ManyToManyField('Member', related_name='member_def')
    #member = models.ForeignKey(Member, on_delete=models.CASCADE)




    
    
