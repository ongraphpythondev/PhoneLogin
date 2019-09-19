from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for  User model with no email and username field."""

    fieldsets = (
        (None, {'fields': ('phone_no', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_no', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_no', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone_no', 'first_name', 'last_name')
    ordering = ('phone_no',)