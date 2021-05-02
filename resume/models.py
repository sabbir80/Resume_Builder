from django.db import models
from ckeditor.fields import RichTextField

class User(models.Model):
    first_name=models.CharField(max_length=20,default=None,null=True)
    last_name = models.CharField(max_length=20,default=None,null=True)
    email= models.EmailField(max_length=20,default=None,null=True)
    company_name= models.CharField(max_length=20,default=None,null=True)
    phone= models.CharField(max_length=20,default=None,null=True)
    password= models.CharField(max_length=20)
    def __str__(self):
        return self.first_name

    @staticmethod
    def get_id_by_mail(email):
        return User.objects.get(email=email)
    @staticmethod
    def get_id_by_id(id):
        return User.objects.get(id=id)

class Personal_info(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    profession=models.CharField(max_length=20,default=None,null=True)
    address=models.CharField(max_length=20,default=None,null=True)
    phone=models.CharField(max_length=20,default=None,null=True)
    email=models.EmailField(max_length=20,default=None,null=True)
    image=models.ImageField(upload_to="upload/image/",default=None,null=True)




    @staticmethod
    def get_id_by_id(id):
        return Personal_info.objects.get(id=id)
class Work_history(models.Model):
    personal_info_id=models.ForeignKey(Personal_info,on_delete=models.CASCADE,default=None,null=True)
    job_title = models.CharField(max_length=20, default=None, null=True)
    employer = models.CharField(max_length=20, default=None, null=True)
    work_description = models.TextField(max_length=255, default=None, null=True)
    start_date=models.DateField(default=None,null=True)
    end_date=models.DateField(default=None,null=True)
    no_experience=models.BooleanField(null=True)
    still_working=models.BooleanField(null=True)

class Education(models.Model):
    personal_info_id=models.ForeignKey(Personal_info,on_delete=models.CASCADE,default=None,null=True)
    institute_name = models.CharField(max_length=20, default=None, null=True)
    institute_location = models.CharField(max_length=20, default=None, null=True)
    degree = models.CharField(max_length=20, default=None, null=True)
    field_of_study=models.CharField(max_length=20,default=None,null=True)
    graduation_start_date=models.DateField(default=None, null=True)
    graduation_end_date = models.DateField(default=None, null=True)
    still_studing = models.BooleanField(null=True)
    description=models.TextField(max_length=255, default=None, null=True)

class Skill(models.Model):
    personal_info_id = models.ForeignKey(Personal_info, on_delete=models.CASCADE, default=None, null=True)
    skill= models.CharField(max_length=20, default=None, null=True)
class Summary(models.Model):
    personal_info_id = models.ForeignKey(Personal_info, on_delete=models.CASCADE, default=None, null=True)
    backgound_description=models.TextField(max_length=255, default=None, null=True)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    job_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    job_details = RichTextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.job_title

class Applicant(models.Model):
    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    profession=models.CharField(max_length=20,default=None,null=True)
    address=models.CharField(max_length=20,default=None,null=True)
    phone=models.CharField(max_length=20,default=None,null=True)
    email=models.EmailField(max_length=20,default=None,null=True)
    resume=models.FileField(upload_to="upload/file/",default=None,null=True)

    def __str__(self):
        return self.email
