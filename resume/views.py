from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'signup.html')