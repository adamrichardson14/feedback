from django.shortcuts import render
from .models import Survey
from django.template import context

def questions(request):
    return render(request, 'survey/questions.html')

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
    
    #Number of Responses
    responses = Survey.objects.all().values_list('nps', flat=True)
    responses = int(len(responses))
    
    #Calculate NPS
    nps = Survey.objects.all().values_list('nps', flat=True)
    nps = calculate_nps(nps)
    #Service score 
    service = Survey.objects.all().values_list('service', flat=True)
    service = detractor(service)
    #Cleanliness score
    cleanliness = Survey.objects.all().values_list('cleanliness', flat=True)
    cleanliness = detractor(cleanliness)
    #Dinner Quality
    dinnerqual = Survey.objects.all().values_list('dinnerqual', flat=True)
    dinnerqual = detractor(dinnerqual)
    #Dinner Service
    dinnerservice = Survey.objects.all().values_list('dinnerservice', flat=True)
    dinnerservice = detractor(dinnerservice)
    #Breakfast Quality
    breakfastqual = Survey.objects.all().values_list('breakfastqual', flat=True)
    breakfastqual = detractor(breakfastqual)
    #Breakfast Service
    breakfastservice = Survey.objects.all().values_list('breakfastservice', flat=True)
    breakfastservice = detractor(breakfastservice)
    #TM Exceeds 
    tmexceeds = Survey.objects.filter(tmexceed=True).count()
    total = Survey.objects.count()
    tmexceed = round((tmexceeds / total)*100, 2)

    feedback = Survey.objects.order_by('-date_submitted').exclude(anyfeedback__isnull=True).exclude(anyfeedback__exact="")

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
        'service': service
    }
   
    return render(request, 'survey/dashboard.html', context)

