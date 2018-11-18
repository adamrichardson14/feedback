from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Survey
from account.models import Profile
from django import forms
from .forms import SurveyForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        x = round(target - measure, 2)
        return x 
    
    object = Survey.objects.filter(sitecode=request.user.pk)
    
    target = Profile.objects.filter(user=request.user.pk)
    #Number of Responses
    responses = object.values_list('nps', flat=True)
    responses = int(len(responses))
    
    #Calculate NPS
    nps = object.values_list('nps', flat=True)
    nps = calculate_nps(nps)
    #Service score 
    service = object.values_list('service', flat=True)
    service = detractor(service)
    servicetarget = target.values_list('servicetarget', flat=True)[0]
    servicevariance = variance(servicetarget, service)
    #Cleanliness score
    cleanliness = object.values_list('cleanliness', flat=True)
    cleanliness = detractor(cleanliness)
    cleanlinesstarget = target.values_list('cleanlinesstarget', flat=True)[0]
    cleanlinessvariance = variance(cleanlinesstarget, cleanliness)

    #Dinner Quality
    dinnerqual = object.values_list('dinnerqual', flat=True)
    dinnerqual = detractor(dinnerqual)
    #Dinner Service
    dinnerservice = object.values_list('dinnerservice', flat=True)
    dinnerservice = detractor(dinnerservice)
    #Breakfast Quality
    breakfastqual = object.values_list('breakfastqual', flat=True)
    breakfastqual = detractor(breakfastqual)
    #Breakfast Service
    breakfastservice = object.values_list('breakfastservice', flat=True)
    breakfastservice = detractor(breakfastservice)
    #TM Exceeds 
    tmexceeds = object.filter(tmexceed=True).count()
    total = object.count()
    tmexceed = round((tmexceeds / total)*100, 2)
    feedback = object.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")




    context = {
        'feedback': feedback,
        'tmexceed': tmexceed,
        'responses': responses,
        'dinnerqual': dinnerqual,
        'dinnerservice': dinnerservice,
        'breakfastqual': breakfastqual,
        'breakfastservice': breakfastservice,
        'cleanliness': cleanliness,
        'nps': nps,
        'service': service, 
        'servicevariance': servicevariance,
        'servicetarget': servicetarget,
        'cleanlinessvariance': cleanlinessvariance,
        'cleanlinesstarget': cleanlinesstarget
    }

    return render(request, 'survey/dashboard.html', context)

def comments(request):
    object = Survey.objects.filter(sitecode=request.user.pk)
    feedback = object.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")
    context = {
        'feedback': feedback
    }

    return render(request, 'survey/comments.html', context)
