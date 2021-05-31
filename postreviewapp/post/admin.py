from django.contrib import admin

# Register your models here.
from .models import udetails
from .models import curntUser
from .models import postdb

admin.site.register(udetails)
admin.site.register(curntUser)
admin.site.register(postdb)