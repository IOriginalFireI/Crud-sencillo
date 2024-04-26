from django import forms
from .models import *

class formulario_curso(forms.ModelForm):
    
    class Meta:
        
        model = curso
        fields = ['codigo', 'nombre', 'creditos']