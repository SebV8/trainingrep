from typing import OrderedDict
from django import forms
from entrenamiento.models import *

class Pr_detailForm(forms.ModelForm):
    class Meta:
        model = Pr_detail
        fields = ('name', 'weight', 'reps', 'date')
        ordering = ('date', 'name')
        
        
class Rm_detailForm(forms.ModelForm):
    class Meta:
        model = Rm_detail
        fields = ('name', 'weight', 'reps', 'date')
        
class TimeCap_detailForm(forms.ModelForm):
    class Meta:
        model = TimeCap_detail
        fields = ('name', 'time', 'date')