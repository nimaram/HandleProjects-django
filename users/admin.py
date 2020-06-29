from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import UserChangeForm,UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['talents','email','is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        ['اطلاعات اصلی',{'fields':['talents','email','password']}],
        ['اطلاعات شخصی',{'fields':['is_active']}],
        ['دسترسی ها',{'fields':['is_admin']}],
    ]
    add_fieldsets = [
        [None,{
            'fields' : ('talents','email','password')
        }]
    ]
    search_fields = ['email','talents']
    ordering = ['email']
    filter_horizontal = []

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
