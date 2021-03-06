from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from resume.middlewares.auth import auth_middleware

# Create your views here.
from resume.models import User,Personal_info,Work_history


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
        #print(user.id)
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
        id=request.session.get('user_id')
        fname=postdata.get('fname')
        lname=postdata.get('lname')
        profession=postdata.get('proff')
        address=postdata.get('address')
        phone=postdata.get('phone')
        email=postdata.get('email')
        image=postdata.get('image')

        customar=Personal_info(user_id=User.get_id_by_id(id),first_name=fname,last_name=lname,profession=profession,address=address,phone=phone,email=email,image=image)
        customar.save()
        request.session['person_pk']=customar.id
        #print(request.session['person_pk'])
        return redirect('form_work')

    return render(request,'form_page.html')
def checkbox(checkbox):
    if checkbox=="on":
        return True
    else:return False
@auth_middleware
def from_work(request):

    if request.method=="POST":
        postdata=request.POST
        id=request.session.get('person_pk')
        job_title=postdata.get('title')
        employer=postdata.get('emp')
        job_description=postdata.get('wd')
        start_date=postdata.get('sd')
        end_date=postdata.get('ed')
        still_working=postdata.get('running')
        no_exp=postdata.get('ne')


        if no_exp:
            customar=Work_history(no_experience=checkbox(no_exp),personal_info_id=Personal_info.get_id_by_id(id))
            customar.save()
            return redirect('form_edu')
        elif still_working:
            customar=Work_history(personal_info_id=Personal_info.get_id_by_id(id),job_title=job_title,employer=employer,work_description=job_description,start_date=start_date,still_working=checkbox(still_working))
            customar.save()
            return redirect('form_edu')
        else:
            customar=Work_history(personal_info_id=Personal_info.get_id_by_id(id),job_title=job_title,employer=employer,work_description=job_description,start_date=start_date,end_date=end_date)
            customar.save()
            return redirect('form_edu')

    return render(request,'form_page_work.html')
@auth_middleware
def from_edu(request):
    return render(request,'form_page_edu.html')
@auth_middleware
def from_skill(request):
    return render(request,'form_page_skill.html')
@auth_middleware
def from_summary(request):
    return render(request,'form_page_summary.html')
@auth_middleware
def resume1(request):
    pid=request.session.get('person_pk')
    person=Personal_info.objects.filter(id=20)



    return render(request,'Resume/resume1.html',{'data':person})
