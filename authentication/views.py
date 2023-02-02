from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Services,ImageSlider

# Create your views here.
def home(request):
    return render(request, "authentication/index1.html")

def signup(request):
    print("test")

    if request.method == "POST":
       # username = request.Post.get('username')
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       myuser = User.objects.create_user(username,email,pass1)
       myuser.first_name = fname
       myuser.last_name = lname

       myuser.save()

       messages.success(request,"Your account has been successfully creted.")
       return redirect('/signin')

    return render(request, "authentication/index1.html")

def signin(request):

    if request.user.is_authenticated:
        return render(request,"authentication/dashboard1.html",{})
    
    
    # Do something for anonymous users.
    
    elif request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            print("testing1")
            login(request, user)
            fname = user.first_name
            return render(request,"authentication/dashboard1.html",{'fname': fname})

        else:
            print("testing2")
            messages.error(request,"Bad Credentials")
            return redirect('home')
    else:
        return render(request, "authentication/signin1.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def home_page(request):
    a = ImageSlider.objects.all()
    Imageslider_data = {
        'data':a
    }
    return render(request,"authentication/smartenweb_homepage.html",Imageslider_data)

def company_page(request):
    return render(request,"authentication/smartenweb_company.html")

def services_page(request):
    a = Services.objects.all()
    services_data = {
        'data':a
    }
    return render(request,"authentication/smartenweb_services.html",services_data)

def contactus_page(request):
    return render(request,"authentication/smartenweb_contactus.html")

def profile_page(request):
    return render(request,"authentication/profile.html")

def calendar_page(request):
    return render(request,"authentication/calendar.html")

def widgets_page(request):
    return render(request,"authentication/widgets.html")

def services_article_page(request):
    return render(request,"authentication/services_article_upload.html")
    
def homepage_imageslider(request):
    return render(request,"authentication/homepage_imageslider.html")

