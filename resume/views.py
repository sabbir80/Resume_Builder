from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from resume.middlewares.auth import auth_middleware

# Create your views here.
from resume.models import User,Personal_info


def home(request):
    return render(request,'home.html')
def registration(request):
    print(request.method)
    if request.method=='POST':
        postdata=request.POST
        f_name=postdata.get('Fname')
        l_name=postdata.get('Lname')
        email=postdata.get('email')
        company_name=postdata.get('Cname')
        phone=postdata.get('phone')
        password=make_password(postdata.get('password'))
        massege = None

        user=User(first_name=f_name,last_name=l_name,email=email,company_name=company_name,phone=phone,password=password)
        if User.objects.filter(email=email).exists():
            massege="you have already register"
            return render(request,'signup.html',{'mg':massege})
        user.save()
        return render(request,'signup.html')

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
                request.session['user_id']=user.id
                print(request.session.get('user_id'))
                return render(request,'home.html')
            else:
                massege="password incorrect"
            return render(request,'login.html',{'mg':massege})

    return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('home')

@auth_middleware
def form(request):
    if request.method=='POST':
        postdata=request.POST
        fname=postdata.get('fname')
        lname=postdata.get('lname')
        profession=postdata.get('proff')
        address=postdata.get('address')
        phone=postdata.get('phone')
        email=postdata.get('email')
        image=postdata.get('image')

        customar=Personal_info(first_name=fname,last_name=lname,profession=profession,address=address,phone=phone,email=email,image=image)
        customar.save()
        return render(request,'form_page.html')

    return render(request,'form_page.html')
