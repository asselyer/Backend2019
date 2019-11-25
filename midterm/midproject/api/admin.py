from django.contrib import admin
from api.models import MainUser, UserProfile, Product, Service
from django.contrib.auth.admin import UserAdmin


class InlineProfile(admin.StackedInline):
    model = UserProfile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    inlines = [InlineProfile,]


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'user', 'address')

admin.site.register(Product)
admin.site.register(Service)
