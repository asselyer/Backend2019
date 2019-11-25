from django.contrib import admin
from api.models import MainUser, Profile, ProjectMember, Task, Project, Block, TaskComment, TaskDocument
from django.contrib.auth.admin import UserAdmin


class InlineProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    inlines = [InlineProfile,]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'web_site', 'avatar', 'user',)

admin.site.register(ProjectMember)
admin.site.register(Block)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(TaskDocument)