from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Topics)
admin.site.register(Departments)
admin.site.register(Agents)
admin.site.register(Tickets)