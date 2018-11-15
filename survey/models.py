from django.db import models
from datetime import datetime

class Survey(models.Model):
    company = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length= 100, blank= True)
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



    
    