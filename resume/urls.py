from django.urls import path

from resume import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.registration,name='ragistration'),
    path('',views.home , name='home'),
    path('form', views.form , name='form'),
    path('logout',views.logout, name='logout')
]