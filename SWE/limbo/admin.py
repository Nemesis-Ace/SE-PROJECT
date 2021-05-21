from django.contrib import admin
from limbo.models import Student,Course,Mark,Addon,Schedule,Instructor,DefaultList,DueList,HostelAllot,LoanList
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Mark)
admin.site.register(Addon)
admin.site.register(Schedule)
admin.site.register(Instructor)
admin.site.register(DefaultList)
admin.site.register(DueList)
admin.site.register(HostelAllot)
admin.site.register(LoanList)
