from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
   class Meta:
    model = JobApplication
    fields = [
        'company_name',
        'role',
        'date_applied',
        'status',
        'job_url',
        'notes',
    ]
    widgets = {
        'date_applied': forms.DateInput(attrs={'type': 'date'}),
    }