from django.contrib import admin

from .models import NewUser


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = NewUser
    list_display = ('email', 'username', 'first_name',)


admin.site.register(NewUser, UserAdmin)
