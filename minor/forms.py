from .models import Logg
from django import forms
class Myforms(forms.ModelForm):

    class Meta:
        model=Logg
        fields=('name','department','authid','question')
        #fields="__all__"
        #exclude=['title']