from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Survey
from account.models import Profile
from django import forms
from .forms import SurveyForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

def questions(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('questions')
 
    else:
 
        form = SurveyForm()
 
        return render(request, "survey/questions.html", {'form': form})


@login_required
def dashboard(request):    
    def detractor(obj):
        s = 0
        for i in obj:
            if (i ==5):
                s += 1
            elif (i == 1):
                s -= 1
        num = round((s / len(obj))*100, 2)
        return num

    def calculate_nps(obj):
        x = 0 
        for i in obj:
            if (i >= 9):
                x = x + 1
            elif (i <=6 ):
                x = x - 1
        nps = round((x / len(obj))*100, 2)
        return nps

        #Variance 

    def variance(target, measure):
        x = round(measure - target, 2)
        return x 

    today = datetime.now()

    def countobject(time, values):
        x = time.values_list(values, flat=True)
        x = int(len(x))
        return x

    def queryobject(time, values):
        y = time.values_list(values, flat=True)
        y = detractor(y)
        return y 

    def npsobject(time, values):
        y = time.values_list(values, flat=True)
        y = calculate_nps(y)
        return y 
    #month objects
    currentmonthobject = Survey.objects.filter(sitecode=request.user.pk, date_submitted__year=today.year, date_submitted__month=today.month)
    currentyearobject = Survey.objects.filter(sitecode=request.user.pk, date_submitted__year=today.year)    
    target = Profile.objects.filter(user=request.user.pk)

    #Monthly Score
    mresponses = countobject(currentmonthobject, 'nps')
    mnps = npsobject(currentmonthobject, 'nps')
    mservice = queryobject(currentmonthobject, 'service')
    mcleanliness = queryobject(currentmonthobject, 'cleanliness')
    mdinnerqual = queryobject(currentmonthobject, 'dinnerqual')
    mdinnerservice = queryobject(currentmonthobject, 'dinnerservice')
    mbreakfastqual = queryobject(currentmonthobject, 'breakfastqual')
    mbreakfastservice = queryobject(currentmonthobject, 'breakfastservice')
    mtmexceeds = currentmonthobject.filter(tmexceed=True).count()
    mtotal = currentmonthobject.count()
    mtmexceed = round((mtmexceeds / mtotal)*100, 2)
    mfeedback = currentmonthobject.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")


    #Year to date scores
    yresponses = countobject(currentyearobject, 'nps')
    ynps = npsobject(currentyearobject, 'nps')
    yservice = queryobject(currentyearobject, 'service')
    ycleanliness = queryobject(currentyearobject, 'cleanliness')
    ydinnerqual = queryobject(currentyearobject, 'dinnerqual')
    ydinnerservice = queryobject(currentyearobject, 'dinnerservice')
    ybreakfastqual = queryobject(currentyearobject, 'breakfastqual')
    ybreakfastservice = queryobject(currentyearobject, 'breakfastservice')
    ytmexceeds = currentyearobject.filter(tmexceed=True).count()
    ytotal = currentyearobject.count()
    ytmexceed = round((ytmexceeds / ytotal)*100, 2)
    yfeedback = currentyearobject.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")



    servicetarget = target.values_list('servicetarget', flat=True)[0]
    servicevariance = variance(servicetarget, yservice)
    #Cleanliness score

    cleanlinesstarget = target.values_list('cleanlinesstarget', flat=True)[0]
    cleanlinessvariance = variance(cleanlinesstarget, ycleanliness)



    context = {
        'mfeedback': mfeedback,
        'mtmexceed': mtmexceed,
        'mresponses': mresponses,
        'mdinnerqual': mdinnerqual,
        'mdinnerservice': mdinnerservice,
        'mbreakfastqual': mbreakfastqual,
        'mbreakfastservice': mbreakfastservice,
        'mcleanliness': mcleanliness,
        'mnps': mnps,
        'mservice': mservice, 
        'servicevariance': servicevariance,
        'servicetarget': servicetarget,
        'cleanlinessvariance': cleanlinessvariance,
        'cleanlinesstarget': cleanlinesstarget,
        'yfeedback': yfeedback,
        'ytmexceed': ytmexceed,
        'yresponses': yresponses,
        'ydinnerqual': ydinnerqual,
        'ydinnerservice': ydinnerservice,
        'ybreakfastqual': ybreakfastqual,
        'ybreakfastservice': ybreakfastservice,
        'ycleanliness': ycleanliness,
        'ynps': ynps,
        'yservice': yservice, 
    }

    return render(request, 'survey/dashboard.html', context)

def comments(request):
    object = Survey.objects.filter(sitecode=request.user.pk)
    feedback = object.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")
    context = {
        'feedback': feedback
    }

    return render(request, 'survey/comments.html', context)
