from django.urls import path

from resume import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/',views.registration,name='ragistration')
]