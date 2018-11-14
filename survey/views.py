from django.shortcuts import render
from .models import Survey
from django.template import context

def questions(request):
    return render(request, 'survey/questions.html')


def dashboard(request):

    nps = Survey.objects.all().values_list('nps', flat=True)

    x = 0
    for i in nps:
        if (i >= 9):
            x = x + 1
        elif (i <=6 ):
            x = x - 1

    def calculate_nps(a, c):
        y = float((a / c)*100)
        return y
    
    nps = round(calculate_nps(x, len(nps)), 2)

    #Service score 
    service = Survey.objects.all().values_list('service', flat=True)

    def detractor(obj):
        s = 0
        for i in obj:
            if (i ==5):
                s += 1
            elif (i == 1):
                s -= 1
        num = round((s / len(obj))*100, 2)
        return num

    service = detractor(service)

    #Cleanliness score

    cleanliness = Survey.objects.all().values_list('cleanliness', flat=True)
    cleanliness = detractor(cleanliness)

    context = {
        'cleanliness': cleanliness,
        'nps': nps,
        'service': service
    }
   
    return render(request, 'survey/dashboard.html', context)

