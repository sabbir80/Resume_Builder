from django.urls import path

from resume import views

urlpatterns = [
    path('', views.login,name='login'),
    path('signup/',views.registration,name='ragistration'),
    path('home',views.home,name='home')
]