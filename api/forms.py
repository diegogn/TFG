from django import forms

class CreateForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    zona_horaria = forms.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre+self.zona_horaria
