from django.contrib import admin
from . models import studentDataTable,companyDataTable,flyerdata,studentfavorite,studentapply,message,StuNotification,ComNotification

admin.site.register(studentDataTable)
admin.site.register(companyDataTable)
admin.site.register(flyerdata)
admin.site.register(studentfavorite)
admin.site.register(studentapply)
admin.site.register(message)
admin.site.register(StuNotification)
admin.site.register(ComNotification)


