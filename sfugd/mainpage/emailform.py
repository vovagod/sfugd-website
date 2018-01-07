#-*- coding: utf-8 -*-
from django import forms

class E_form(forms.Form):
    e_name = forms.CharField(max_length=100)
    e_mail = forms.EmailField()
    e_subject = forms.CharField(max_length=100)
    e_message = forms.CharField(widget=forms.Textarea)
