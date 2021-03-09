from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=20,default=None,null=True)
    last_name = models.CharField(max_length=20,default=None,null=True)
    email= models.EmailField(max_length=20,default=None,null=True)
    company_name= models.CharField(max_length=20,default=None,null=True)
    phone= models.CharField(max_length=20,default=None,null=True)
    password= models.CharField(max_length=20)

    @staticmethod
    def get_id_by_mail(email):
        return User.objects.get(email=email)



