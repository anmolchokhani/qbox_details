from django.contrib import admin
from .models import ClientData

# Register your models here.
@admin.register(ClientData)
class ClientDataAdmin(admin.ModelAdmin):
    list_display= ('boxno','qtrack_email','qtrack_password','sudo_password')


