from django import forms
from .models import *

class TalabaForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=80, label="Ism")
    course = forms.IntegerField(min_value=1, max_value=7, label="Kurs")
    books = forms.IntegerField(min_value=0, max_value=10, label="Kitob soni")
    graduate = forms.BooleanField(label="Bitiruvchimi?", required=False)

class MuallifForm(forms.Form):
    ism = forms.CharField(min_length=3, max_length=80, label="Ism")
    yosh = forms.IntegerField(min_value=1, max_value=120, label="Yosh")
    tirik = forms.ChoiceField(choices=[("ha","ha"),("yo'q","yo'q")])
    kitob_soni = forms.IntegerField(min_value=0)
    jinsi = forms.ChoiceField(choices=[("erkak","erkak"),("ayol","ayol")])
    tugulgan_sana = forms.DateField()

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('__all__')

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('__all__')

class AdminForm(forms.Form):
    ism = forms.CharField(min_length=5, max_length=80, label='Ism')
    ish_vaqti = forms.CharField(min_length=5, max_length=20, label='Ish vaqti')

