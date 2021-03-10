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

class Personal_info(models.Model):
    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    profession=models.CharField(max_length=20,default=None,null=True)
    address=models.CharField(max_length=20,default=None,null=True)
    phone=models.CharField(max_length=20,default=None,null=True)
    email=models.EmailField(max_length=20,default=None,null=True)
    image=models.ImageField(upload_to='upload/profile_pic',blank=True,null=True)

    def __str__(self):
        return self.email
class Work_history(models.Model):
    job_title = models.CharField(max_length=20, default=None, null=True)
    employer = models.CharField(max_length=20, default=None, null=True)
    work_description = models.TextField(max_length=255, default=None, null=True)
    start_date=models.DateField(default=None,null=True)
    end_date=models.DateField(default=None,null=True)
    no_experience=models.BooleanField(null=True)
    still_working=models.BooleanField(null=True)

class Education(models.Model):
    institute_name = models.CharField(max_length=20, default=None, null=True)
    institute_location = models.CharField(max_length=20, default=None, null=True)
    degree = models.CharField(max_length=20, default=None, null=True)
    field_of_study=models.CharField(max_length=20,default=None,null=True)
    graduation_start_date=models.DateField(default=None, null=True)
    graduation_end_date = models.DateField(default=None, null=True)
    still_working = models.BooleanField(null=True)
    description=models.TextField(max_length=255, default=None, null=True)

class Skill(models.Model):
    skill= models.CharField(max_length=20, default=None, null=True)
class Summary(models.Model):
    backgound_description=models.TextField(max_length=255, default=None, null=True)

