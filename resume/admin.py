from django.contrib import admin

from resume.models import User, Personal_info, Work_history, Education, Skill,Summary,Post,Applicant

admin.site.register(User)
admin.site.register(Personal_info)
admin.site.register(Work_history)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Summary)
admin.site.register(Applicant)
class PostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['job_title', 'content']
    prepopulated_fields = {'slug': ('job_title',)}
admin.site.register(Post,PostAdmin)

