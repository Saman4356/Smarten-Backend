from django.db import models
from django.forms import TextInput, EmailInput
from django import forms
class Services(models.Model):
    # services_icon = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Icon', 'style': 'width: 300px;', 'class': 'form-control'}))
    # services_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    # services_des = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Des', 'style': 'width: 300px;', 'class': 'form-control'}))
    services_title=models.CharField(max_length=50)
    services_icon=models.CharField(max_length=50)
    services_des=models.CharField(max_length=100)
    services_image=models.ImageField(blank=True, null=True,upload_to='media/images/')

class ImageSlider(models.Model):
    slider_title=models.CharField(max_length=50)
    slider_image=models.ImageField(upload_to='media/images')
    slider_squ=models.IntegerField()


