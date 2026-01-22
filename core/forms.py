from django import forms
from .models import Job, Freelancer

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'budgetPerHour','hours']


class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['name', 'skill', 'email', 'bio']
