from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
from resume.models import User


def home(request):
    return render(request,'home.html')
def registration(request):
    print(request.method)
    if request.method=='POST':
        postdata=request.POST
        f_name=postdata.get('Fname')
        print(f_name)
        l_name=postdata.get('Lname')
        email=postdata.get('email')
        company_name=postdata.get('Cname')
        phone=postdata.get('phone')
        password=make_password(postdata.get('password'))
        print(f_name,l_name,email,password)

        context={
            'fn':f_name,
            'ln':l_name,
            'email':email,
            'phone':phone,
            'cn':company_name,
            'pass':password

        }


        user=User(first_name=f_name,last_name=l_name,email=email,company_name=company_name,phone=phone,password=password)
        user.save()
        return render(request,'signup.html',context)

    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        postdata=request.POST
        email=postdata.get('email')
        password=postdata.get('password')
        user=User.get_id_by_mail(email)
        massege=None

        if user:
            flag=check_password(password,user.password)
            if flag:
                return render(request,'home.html')
            else:
                massege="password incorrect"
            return render(request,'login.html',{'mg':massege})

    return render(request,'login.html')