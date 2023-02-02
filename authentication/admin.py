from django.contrib import admin
from .models import Services,ImageSlider
class ServicesAdmin(admin.ModelAdmin):
    list_display=('services_icon' , 'services_title' , 'services_des')

admin.site.register(Services ,ServicesAdmin)

class ImageSliderAdmin(admin.ModelAdmin):
    list_display=('slider_title' , 'slider_image' , 'slider_squ')

admin.site.register(ImageSlider ,ImageSliderAdmin)

# Register your models here.
