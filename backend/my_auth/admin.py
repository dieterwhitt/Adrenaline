from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# refer to admin site setup docs

class MyUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ('username', 'email', 'first_name', 'last_name', "birthday", "height", "weight",
                    'is_staff', 'is_active')  # displayed fields
    list_filter = ('is_staff', 'is_active')  # filters
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Register your custom user model
admin.site.register(get_user_model(), MyUserAdmin)
