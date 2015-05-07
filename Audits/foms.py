from django import forms
from models import Question
from django.forms.models import ModelForm

class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100)
    docfile = forms.FileField(
        label='Selecciona un archivo'
    )
    
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['user']
        