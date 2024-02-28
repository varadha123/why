from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'customer/home.html')
def Signup(request):
    return render(request,'customer/signup.html')
