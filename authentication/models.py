from django.db import models
class Services(models.Model):
    services_icon=models.CharField(max_length=50)
    services_title=models.CharField(max_length=50)
    services_des=models.TextField()
    services_image=models.ImageField(upload_to='images')

class ImageSlider(models.Model):
    slider_title=models.CharField(max_length=50)
    slider_image=models.ImageField(upload_to='images')
    slider_squ=models.IntegerField()


