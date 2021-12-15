from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField(max_length=240)
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcather=forms.CharField(required=False,widget=HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean(self) -> str:
    #     dd= super().clean()
    #     em=dd['email']
    #     em2=dd['name']
    #     if em != em2:
    #         raise ValidationError('no nope')

    # def clean_botcather(self):
    #     botcather=self.cleaned_data['botcather']
    #     if len(botcather)>0:
    #         raise ValidationError('you are a bot !!!!')
    #     return botcather