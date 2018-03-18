from django import forms
from fillform.models import fill

class symform(forms.Form):
    symptoms1 = forms.CharField(max_length=128, help_text="Please enter the symptom")
    severety1 = forms.IntegerField( min_value=1,max_value=5,   help_text="Please enter the related sverity")
    symptoms2 = forms.CharField(max_length=128, help_text="Please enter the symptom")
    severety2 = forms.IntegerField( min_value=1,max_value=5,   help_text="Please enter the related sverity")
    symptoms3 = forms.CharField(max_length=128, help_text="Please enter the symptom")
    severety3 = forms.IntegerField( min_value=1,max_value=5,   help_text="Please enter the related sverity")
