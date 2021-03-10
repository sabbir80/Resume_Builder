from django.contrib import admin

from resume.models import User, Personal_info, Work_history, Education, Skill,Summary

admin.site.register(User)
admin.site.register(Personal_info)
admin.site.register(Work_history)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Summary)

