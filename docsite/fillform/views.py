from django.shortcuts import render, redirect
from django.http import HttpResponse
from .HINT_Scraper import disease
from .models import fill
def index(request):
    return render(request,'fillform/index.html')

def createDummy():
    diseases = ['Cancer','Arthritis','Asthma']
    for i in diseases:
        dict1 = disease.symptoms(i)
        dict2 = disease.complications(i)
        dict3 = disease.diagnosis(i)
        data = fill(symptoms = dict1, complications = dict2, diagnosis = dict3)
        data.save()
        return redirect('index')

