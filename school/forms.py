from django import forms
from .models import Material, SerialModel

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class SerialForm(forms.ModelForm):
    class Meta:
        model = SerialModel
        fields = '__all__'
