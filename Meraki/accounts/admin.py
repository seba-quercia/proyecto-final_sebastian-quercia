from django.contrib import admin
from accounts.models import Message, Profile

# Register your models here.

admin.site.register(Message)
admin.site.register(Profile)