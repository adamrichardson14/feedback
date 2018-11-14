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
    
    nps = calculate_nps(x, len(nps))

    context = {
        'nps': nps
    }
   
    return render(request, 'survey/dashboard.html', context)

