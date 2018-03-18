from django.shortcuts import render, redirect
from django.http import HttpResponse
from .HINT_Scraper import disease
from .models import fill
from .forms import symform
from django.views.decorators.http import require_POST
import time
from . import predictor
def req(request):
     form=symform()
     return render(request,'fillform/index.html',{'form':form})
dis = 'Migraine'
def createDummy(i):
     # diseases = ['Asthma','Cancer']
     # for i in diseases:
     dict1 = disease.symptoms(i)
     dict2 = disease.complications(i)
     dict3 = disease.diagnosis(i)
     dict4 = disease.causes(i)
     data = fill(title = i, symptoms = dict1, complications = dict2, diagnosis = dict3, causes = dict4)
     data.save()

@require_POST
def submit(request):
    createDummy(dis)
    rec={}
    dic = {'swell joint':1,'pain joint':1,'pain':1}
    form=symform(request.POST)
    if(form.is_valid()):
        rec[form.cleaned_data['symptoms1']]=int(form.cleaned_data['severety1'])
        rec[form.cleaned_data['symptoms2']]=int(form.cleaned_data['severety2'])
        rec[form.cleaned_data['symptoms3']]=int(form.cleaned_data['severety3'])
        bimaari = predictor.predictor_disease(rec)
        # time.sleep(6)
        return HttpResponse('Thank you! Reach your database for further details.')
