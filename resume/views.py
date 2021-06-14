from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.views import generic
from django.core.mail import send_mail

from resume.middlewares.auth import auth_middleware

# Create your views here.
from resume.models import User,Personal_info,Work_history,Education,Skill,Summary,Post,Applicant

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


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
        file=request.FILES
        id=request.session.get('user_id')
        fname=postdata.get('fname')
        lname=postdata.get('lname')
        profession=postdata.get('proff')
        address=postdata.get('address')
        phone=postdata.get('phone')
        email=postdata.get('email')
        image=file.get('image')
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
    if request.method=='POST':
        postdata=request.POST
        id = request.session.get('person_pk')
        institute_name=postdata.get('Iname')
        institute_location=postdata.get('ILname')
        dgree=postdata.get('dgree')
        field_of_study=postdata.get('FOS')
        graduation_start_date=postdata.get('SD')
        graduation_end_date=postdata.get('ED')
        still_studing=postdata.get('CA')
        description=postdata.get('des')
        if still_studing:
            customar=Education(personal_info_id=Personal_info.get_id_by_id(id),institute_name=institute_name,institute_location=institute_location,degree=dgree,field_of_study=field_of_study,graduation_start_date=graduation_start_date,still_studing=checkbox(still_studing),description=description)
            customar.save()
            return redirect('form_skill')
        else:
            customar=Education(personal_info_id=Personal_info.get_id_by_id(id),institute_name=institute_name,institute_location=institute_location,degree=dgree,field_of_study=field_of_study,graduation_start_date=graduation_start_date,graduation_end_date=graduation_end_date,description=description)
            customar.save()
            return redirect('form_skill')
    return render(request,'form_page_edu.html')
@auth_middleware
def from_skill(request):
    if request.method=='POST':
        postdata=request.POST
        id = request.session.get('person_pk')
        skill=postdata.getlist('skill[]')
        for i in skill:
            user=Skill(personal_info_id=Personal_info.get_id_by_id(id),skill=i)
            user.save()
        return redirect('form_summary')

    return render(request,'form_page_skill.html')
@auth_middleware
def from_summary(request):
    if request.method=='POST':
        id = request.session.get('person_pk')
        postdata=request.POST
        about=postdata.get('about')
        s=Summary(personal_info_id=Personal_info.get_id_by_id(id),backgound_description=about)
        s.save()
        return redirect('resume1')

    return render(request,'form_page_summary.html')
@auth_middleware
def resume1(request):
    pid=request.session.get('person_pk')

    person=Personal_info.objects.filter(id=pid)

    work=Work_history.objects.filter(personal_info_id=pid)
    education=Education.objects.filter(personal_info_id=pid)
    skill=Skill.objects.filter(personal_info_id=pid)
    about = Summary.objects.filter(personal_info_id=pid)
    context={
        'data': person,
        'work':work,
        'education':education,
        'skill':skill,
        'about':about
    }

    return render(request,'Resume/resume1.html',context)
@auth_middleware
def final(request):
    person=Personal_info.objects.all()
    context={
        'person':person
    }
    return render(request,'finalization.html',context)
def render_pdf_view(request):
    pid=request.session.get('person_pk')

    person=Personal_info.objects.filter(id=pid)

    work=Work_history.objects.filter(personal_info_id=pid)
    education=Education.objects.filter(personal_info_id=pid)
    skill=Skill.objects.filter(personal_info_id=pid)
    about = Summary.objects.filter(personal_info_id=pid)
    context={
        'data': person,
        'work':work,
        'education':education,
        'skill':skill,
        'about':about
    }
    template_path = 'Resume/resume1pdf.html'
    #context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def job_apply(request):
    if request.method=='POST':
        try:
            postdata=request.POST
            file=request.FILES
            fname=postdata.get('fname')
            lname=postdata.get('lname')
            profession=postdata.get('proff')
            address=postdata.get('address')
            phone=postdata.get('phone')
            email=postdata.get('email')
            file=file.get('file')
            applicant=Applicant(first_name=fname,last_name=lname,profession=profession,address=address,phone=phone,email=email,resume=file)
            applicant.save()
            mgs='Thank you for applying.We got your Resume,let us go through your Resume and wait for our mail.'
            send_mail('Divine IT Limited',mgs , '17103389@iubat.edu', [email],
                      fail_silently=False)
            return redirect('job_post')
        except:
            print('not not not')
            return render(request,'job_apply.html')


    return render(request,'job_apply.html')
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'job_post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'job_post_details.html'
