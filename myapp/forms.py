from django import forms
from .models import ArticleSubmission

class ArticleSubmissionForm(forms.ModelForm):
    class Meta:
        model = ArticleSubmission
        fields = ['name', 'email', 'title', 'document']


# careers form
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'name', 'email', 'resume', 'message']        
