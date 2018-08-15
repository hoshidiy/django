from django import forms
from .models import Schedule, Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['person','date','hayagaeri_plan','hayagaeri_result']
