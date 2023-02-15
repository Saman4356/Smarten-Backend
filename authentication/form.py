from django import forms
from django.forms import TextInput

from authentication.models import Services,ImageSlider
...

class ServiceForm(forms.ModelForm):
   class Meta:
        model = Services
        fields = ['services_title','services_icon' ,'services_des','services_image']
        widgets = {
            'services_icon': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Icon'
                }),
            'services_title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'services_des': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
                })
        }

class ImageSliderForm(forms.ModelForm):
    class Meta:
        model = ImageSlider
        fields = ['slider_title','slider_image','slider_squ']
        widgets = {
            'slider_title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'slider__squ': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Sequence'
                })
        }
