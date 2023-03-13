from django.contrib import admin
from .models import Clg
from .models import Register
# Register your models here.
admin.site.register(Clg)

class registerAdmin(admin.ModelAdmin):
    list_display = ['name','password','confirm password']


admin.site.register(Register)




