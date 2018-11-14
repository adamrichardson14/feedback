from django.contrib import admin
from account.models import Profile

class AccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, AccountAdmin)