from django.contrib import admin

from accounts.models import Role, UserRole


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    pass
