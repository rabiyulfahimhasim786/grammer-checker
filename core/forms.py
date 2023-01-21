from django import forms
from .models import Grammercheck

class GrammerForm(forms.ModelForm):
    class Meta:
        model = Grammercheck
        fields = '__all__'