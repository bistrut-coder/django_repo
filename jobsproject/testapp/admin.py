from django.contrib import admin

# Register your models here.
from testapp.models import Hybdjobs,Bngjobs,Punejobs
class HybdjobsAdmin(admin.ModelAdmin):
    list_display = ['company','title','phonenumber','email','dob']
admin.site.register(Hybdjobs,HybdjobsAdmin)

class BngjobsAdmin(admin.ModelAdmin):
    list_display = ['company','title','phonenumber','email','dob']
admin.site.register(Bngjobs,BngjobsAdmin)


class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['company','title','phonenumber','email','dob']
admin.site.register(Punejobs,PunejobsAdmin)