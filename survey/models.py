from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ModelForm

class Survey(models.Model):
    email = models.EmailField()
    company = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length= 100, blank= True)
    sitecode = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_submitted = models.DateTimeField(default=datetime.now, blank=True)
    arrival_date = models.DateTimeField(default=datetime.now, blank=True)
    nps = models.IntegerField()
    service = models.IntegerField()
    cleanliness = models.IntegerField()
    checkin = models.IntegerField()
    dinnerqual = models.IntegerField()
    dinnerservice = models.IntegerField()
    breakfastqual = models.IntegerField()
    breakfastservice = models.IntegerField()
    tmexceed = models.BooleanField()
    tmexceeddetails = models.TextField(max_length= 1000, blank=True)
    anyfeedback = models.TextField(max_length= 2500, blank=True)

    def __str__(self):
        return self.site





    
    