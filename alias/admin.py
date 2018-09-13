from django.contrib import admin

from guardian.admin import GuardedModelAdmin
# Register your models here.

class AuthorAdmin(GuardedModelAdmin):
    pass

admin.site.register(AuthorAdmin)