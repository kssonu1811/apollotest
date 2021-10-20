from django.contrib import admin
from .models import Employee, User
from ticketapp.models import Contact, status

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Contact)
admin.site.register(status)