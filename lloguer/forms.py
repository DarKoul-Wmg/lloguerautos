from django import forms
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from django.utils import timezone

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['user', 'automobil', 'data_inicio', 'data_fi']
    
    # usuarios existents
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    
    # automobils existents
    automobil = forms.ModelChoiceField(queryset=Automobil.objects.all(), required=True)

    data_inicio = forms.DateField(initial=timezone.now, widget=forms.DateInput(attrs={'type': 'date'}))
    
    data_fi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
