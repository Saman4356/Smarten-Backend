from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"), 
    path('signout', views.signout, name="signout"),
    path('homepage', views.home_page, name="homepage"),    
    path('company', views.company_page, name="company"),
    path('services', views.services_page, name= "services"),
    path('contactus', views.contactus_page, name= "contactus"),
    path('profile', views.profile_page, name= "profile"), 
    path('calendar', views.calendar_page, name="calendar"),
    path('widgets', views.widgets_page, name="widgets"),
    path('servicesarticle', views.services_article_page, name="servicesarticle"),
    path('homepageimageslider', views.homepage_imageslider, name="homepageimageslider")
    ]