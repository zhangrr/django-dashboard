from django.contrib import admin

# Register your models here.
#from dashboard.models import Vimage, Pmachine, Vmachine, Task
from .models import *
   
admin.site.register(Vimage)
admin.site.register(Pmachine)
admin.site.register(Vmachine)
admin.site.register(Task)
