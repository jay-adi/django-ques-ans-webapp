from django.contrib import admin
from .models import Logg
from django.contrib.auth.models import Group





class LoggAdmin(admin.ModelAdmin):
    list_display=('name','confirm','department')
    list_filter = ('department','confirm',)






admin.site.register(Logg,LoggAdmin)
admin.site.unregister(Group)
admin.site.site_header="TEACHER DASHBOARD"