from django.urls import path

from resume import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.registration,name='ragistration'),
    path('',views.home , name='home'),
    path('form', views.form , name='form'),
    path('logout',views.logout, name='logout'),
    path('form_work', views.from_work , name='form_work'),
    path('form_edu', views.from_edu, name='form_edu'),
    path('form_skill', views.from_skill, name='form_skill'),
    path('form_summary', views.from_summary , name='form_summary'),
    path('template',views.resume1,name='resume1')
]